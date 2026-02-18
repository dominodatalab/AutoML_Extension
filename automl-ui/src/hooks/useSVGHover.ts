import { useRef, useState, useCallback } from 'react'

/**
 * Shared SVG hover logic for chart components.
 * Converts mouse position to a data index and provides tooltip positioning.
 */
export function useSVGHover(width: number, padLeft: number, plotW: number, dataLength: number) {
  const svgRef = useRef<SVGSVGElement>(null)
  const [hoverIndex, setHoverIndex] = useState<number | null>(null)

  const onMouseMove = useCallback((e: React.MouseEvent<SVGSVGElement>) => {
    const svg = svgRef.current
    if (!svg) return
    const rect = svg.getBoundingClientRect()
    const svgX = ((e.clientX - rect.left) / rect.width) * width
    const frac = (svgX - padLeft) / plotW
    if (frac < 0 || frac > 1) { setHoverIndex(null); return }
    setHoverIndex(Math.round(frac * (dataLength - 1)))
  }, [width, padLeft, plotW, dataLength])

  const onMouseLeave = useCallback(() => setHoverIndex(null), [])

  return { svgRef, hoverIndex, onMouseMove, onMouseLeave }
}

/**
 * Compute tooltip CSS left position and transform for edge-aware placement.
 */
export function getTooltipStyle(xPixel: number, width: number) {
  const pct = (xPixel / width) * 100
  return {
    left: `${pct}%`,
    transform: pct > 75 ? 'translateX(-100%)' : pct < 25 ? 'none' : 'translateX(-50%)',
  }
}
