// components/icons/ProductIcons.tsx
import * as React from "react";

export function AddProductIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      viewBox="0 0 64 64"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      {...props}
    >
      <defs>
        <filter id="add-shadow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow
            dx="0"
            dy="4"
            stdDeviation="4"
            floodColor="currentColor"
            floodOpacity="0.2"
          />
        </filter>
        <linearGradient id="add-grad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="currentColor" stopOpacity="0.4" />
          <stop offset="100%" stopColor="currentColor" stopOpacity="0.8" />
        </linearGradient>
      </defs>
      <rect
        x="12"
        y="20"
        width="40"
        height="24"
        rx="4"
        fill="url(#add-grad)"
        stroke="currentColor"
        strokeWidth="2"
        filter="url(#add-shadow)"
      />
      <path
        d="M12 20l20-12 20 12"
        stroke="currentColor"
        strokeWidth="2"
        fill="none"
      />
      <path
        d="M32 28v12M26 34h12"
        stroke="#fff"
        strokeWidth="3"
        strokeLinecap="round"
      />
    </svg>
  );
}

export function DeleteProductIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      viewBox="0 0 64 64"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      {...props}
    >
      <defs>
        <filter id="del-shadow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow
            dx="0"
            dy="4"
            stdDeviation="4"
            floodColor="currentColor"
            floodOpacity="0.2"
          />
        </filter>
        <linearGradient id="del-grad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="currentColor" stopOpacity="0.4" />
          <stop offset="100%" stopColor="currentColor" stopOpacity="0.8" />
        </linearGradient>
      </defs>
      <path
        d="M18 22h28l-4 32H22l-4-32z"
        fill="url(#del-grad)"
        stroke="currentColor"
        strokeWidth="2"
        filter="url(#del-shadow)"
      />
      <path d="M14 22h36" stroke="currentColor" strokeWidth="2" />
      <path
        d="M24 30l16 16M40 30l-16 16"
        stroke="#fff"
        strokeWidth="3"
        strokeLinecap="round"
      />
    </svg>
  );
}

export function UpdateProductIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      viewBox="0 0 64 64"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      {...props}
    >
      <defs>
        <filter id="upd-shadow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow
            dx="0"
            dy="4"
            stdDeviation="4"
            floodColor="currentColor"
            floodOpacity="0.2"
          />
        </filter>
        <radialGradient id="upd-grad" cx="0.5" cy="0.5" r="0.5">
          <stop offset="0%" stopColor="currentColor" stopOpacity="0.4" />
          <stop offset="100%" stopColor="currentColor" stopOpacity="0.8" />
        </radialGradient>
      </defs>
      <circle
        cx="32"
        cy="32"
        r="16"
        fill="url(#upd-grad)"
        stroke="currentColor"
        strokeWidth="2"
        filter="url(#upd-shadow)"
      />
      <path
        d="M21 32a11 11 0 013-8"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
      />
      <path
        d="M24 24l-8 0 0 -8"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
      />
      <path
        d="M43 32a11 11 0 01-3 8"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
      />
      <path
        d="M40 40l8 0 0 8"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
      />
    </svg>
  );
}

export function ViewProductIcon(props: React.SVGProps<SVGSVGElement>) {
  return (<svg
    viewBox="0 0 64 64"
    fill="none"
    stroke="currentColor"
    strokeLinecap="round"
    strokeLinejoin="round"
    {...props}
  >
    {/* product box */}
    <rect x="2" y="4" width="48" height="48" rx="2" ry="2" />
    {/* magnifier lens */}
    <circle cx="17" cy="7" r="20" />
    {/* magnifier handle */}
    <line x1="19.2" y1="9.2" x2="22" y2="12" />
  </svg>)
}