/**
 * Build a Domino tenant URL for user-facing links.
 * - If VITE_DOMINO_API_HOST is provided at build time (derived from DOMINO_API_HOST),
 *   use that host for all links.
 * - Otherwise, derive the tenant host from window.location by stripping an apps. prefix.
 */
export function toDominoTenantUrl(rawUrl?: string): string | null {
  if (!rawUrl) return null
  try {
    // Prefer explicitly provided host from dev env if set
    const envHost = (import.meta.env as any).VITE_DEV_DOMINO_API_HOST as string | undefined

    let base = new URL(window.location.origin)
    if (envHost && envHost.trim().length > 0) {
      const envUrl = new URL(envHost)
      base = envUrl
    } else if (base.hostname.startsWith('apps.')) {
      // Domino Apps subdomain → tenant hostname
      base.hostname = base.hostname.slice('apps.'.length)
    }

    const url = new URL(rawUrl, base.origin)
    url.protocol = base.protocol
    url.hostname = base.hostname
    url.port = base.port
    return url.toString()
  } catch {
    return rawUrl
  }
}

