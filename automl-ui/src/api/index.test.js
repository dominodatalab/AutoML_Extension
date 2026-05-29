import assert from 'node:assert/strict'
import { afterEach, describe, it } from 'node:test'

import api, { getApiRedirectTarget } from './index.ts'

const originalFetch = globalThis.fetch
const originalWindow = globalThis.window
const originalConsoleError = console.error

afterEach(() => {
  globalThis.fetch = originalFetch
  console.error = originalConsoleError

  if (originalWindow === undefined) {
    delete globalThis.window
  } else {
    globalThis.window = originalWindow
  }
})

function setWindowLocation(href) {
  const url = new URL(href)
  const assignedUrls = []

  globalThis.window = {
    location: {
      href: url.href,
      pathname: url.pathname,
      search: url.search,
      assign: (target) => {
        assignedUrls.push(target)
      },
    },
  }

  return assignedUrls
}

describe('getApiRedirectTarget', () => {
  it('replaces an existing callback query parameter with the encoded current location', () => {
    const currentLocation = 'https://domino.example.com/apps/automl?projectId=project-1&tab=jobs'
    const response = new Response(null, {
      status: 302,
      headers: {
        Location: '/login?callback=old-callback&state=state-1',
      },
    })

    const target = getApiRedirectTarget(
      response,
      '/apps/automl/svc/v1/jobs',
      currentLocation
    )

    assert.ok(target)
    assert.ok(target.includes(`callback=${encodeURIComponent(currentLocation)}`))

    const targetUrl = new URL(target)
    assert.equal(targetUrl.origin, 'https://domino.example.com')
    assert.equal(targetUrl.pathname, '/login')
    assert.equal(targetUrl.searchParams.get('callback'), currentLocation)
    assert.equal(targetUrl.searchParams.get('state'), 'state-1')
  })

  it('only creates a redirect target for a 302 response with a Location header', () => {
    const currentLocation = 'https://domino.example.com/apps/automl'
    const requestUrl = '/apps/automl/svc/v1/jobs'

    assert.equal(
      getApiRedirectTarget(
        new Response(null, { status: 200, headers: { Location: '/login?callback=old' } }),
        requestUrl,
        currentLocation
      ),
      undefined
    )
    assert.equal(
      getApiRedirectTarget(new Response(null, { status: 302 }), requestUrl, currentLocation),
      undefined
    )
    assert.equal(
      getApiRedirectTarget(
        new Response(null, { status: 302, headers: { Location: '/login?callback=old' } }),
        requestUrl,
        currentLocation
      ),
      'https://domino.example.com/login?callback=https%3A%2F%2Fdomino.example.com%2Fapps%2Fautoml'
    )
  })
})

describe('api redirect handling', () => {
  it('requests manual redirect handling so the client can inspect 302 responses', async () => {
    const assignedUrls = setWindowLocation('https://domino.example.com/apps/automl')
    const fetchCalls = []

    globalThis.fetch = async (...args) => {
      fetchCalls.push(args)
      return new Response(null, { status: 204 })
    }

    await api.get('jobs')

    assert.equal(assignedUrls.length, 0)
    assert.equal(fetchCalls.length, 1)
    assert.equal(fetchCalls[0][0], '/apps/automl/svc/v1/jobs')
    assert.equal(fetchCalls[0][1].method, 'GET')
    assert.equal(fetchCalls[0][1].credentials, 'include')
    assert.equal(fetchCalls[0][1].redirect, 'manual')
  })

  it('redirects the browser after a 302 response and writes the current location into callback', async () => {
    const currentLocation = 'https://domino.example.com/apps/automl?projectId=project-1'
    const assignedUrls = setWindowLocation(currentLocation)
    console.error = () => {}

    globalThis.fetch = async () => new Response(null, {
      status: 302,
      headers: {
        Location: '/login?callback=old-callback&state=state-1',
      },
    })

    await assert.rejects(api.get('jobs'), /Redirecting after API 302 response/)

    assert.equal(assignedUrls.length, 1)

    const assignedUrl = new URL(assignedUrls[0])
    assert.equal(assignedUrl.origin, 'https://domino.example.com')
    assert.equal(assignedUrl.pathname, '/login')
    assert.equal(assignedUrl.searchParams.get('callback'), currentLocation)
    assert.equal(assignedUrl.searchParams.get('state'), 'state-1')
  })
})
