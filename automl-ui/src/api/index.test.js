import assert from 'node:assert/strict'
import { afterEach, describe, it } from 'node:test'

import api from './index.ts'

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
  let reloadCount = 0

  globalThis.window = {
    location: {
      href: url.href,
      pathname: url.pathname,
      search: url.search,
      reload: () => {
        reloadCount += 1
      },
    },
  }

  return {
    get reloadCount() {
      return reloadCount
    },
  }
}

describe('api redirect handling', () => {
  it('requests manual redirect handling so the client can inspect 302 responses', async () => {
    const location = setWindowLocation('https://domino.example.com/apps/automl')
    const fetchCalls = []

    globalThis.fetch = async (...args) => {
      fetchCalls.push(args)
      return new Response(null, { status: 204 })
    }

    await api.get('jobs')

    assert.equal(location.reloadCount, 0)
    assert.equal(fetchCalls.length, 1)
    assert.equal(fetchCalls[0][0], '/apps/automl/svc/v1/jobs')
    assert.equal(fetchCalls[0][1].method, 'GET')
    assert.equal(fetchCalls[0][1].credentials, 'include')
    assert.equal(fetchCalls[0][1].redirect, 'manual')
  })

  it('refreshes the browser after a 302 response to app consent', async () => {
    const location = setWindowLocation('https://domino.example.com/apps/automl?projectId=project-1')
    console.error = () => {}

    globalThis.fetch = async () => new Response(null, {
      status: 302,
      headers: {
        Location: '/app-consent?callback=old-callback&state=state-1',
      },
    })

    await assert.rejects(api.get('jobs'), /Refreshing after API 302 response/)

    assert.equal(location.reloadCount, 1)
  })

  it('does not refresh the browser after a 302 response to a different location', async () => {
    const location = setWindowLocation('https://domino.example.com/apps/automl')
    console.error = () => {}

    globalThis.fetch = async () => new Response(null, {
      status: 302,
      headers: {
        Location: '/login?callback=old-callback',
      },
    })

    await assert.rejects(api.get('jobs'))

    assert.equal(location.reloadCount, 0)
  })

  it('does not refresh the browser for non-302 responses', async () => {
    const location = setWindowLocation('https://domino.example.com/apps/automl')
    console.error = () => {}

    globalThis.fetch = async () => new Response(
      JSON.stringify({ detail: 'Unauthorized' }),
      {
        status: 401,
        headers: {
          'Content-Type': 'application/json',
          Location: '/login?callback=old-callback',
        },
      }
    )

    await assert.rejects(api.get('jobs'), /Unauthorized/)

    assert.equal(location.reloadCount, 0)
  })
})
