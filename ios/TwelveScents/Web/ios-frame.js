// App build of ios-frame.js: IOSDevice renders its children full-bleed on the real device
// (no simulated bezel, notch, status bar or home indicator - iOS draws those).
(function () {
  const h = (...a) => window.React.createElement(...a);
  function IOSDevice({ children }) {
    return h('div', { style: { width: '100%', height: '100dvh', position: 'relative', overflow: 'hidden' } }, children);
  }
  function IOSStatusBar() { return null; }
  Object.assign(window, { IOSDevice, IOSStatusBar });
})();
