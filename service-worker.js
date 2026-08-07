const CACHE = "doc2audio-v1";
const ASSETS = ["./","./index.html","./manifest.webmanifest",
  "./icons/icon-192.png","./icons/icon-512.png","./icons/maskable-512.png",
  "./icons/apple-touch-180.png","./icons/favicon-32.png"];
self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  const u = new URL(e.request.url);
  if (u.origin === location.origin) {            // app shell: offline-first
    e.respondWith(caches.match(e.request).then(r => r || fetch(e.request).then(resp => {
      const copy = resp.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); return resp;
    }).catch(() => caches.match("./index.html"))));
  }                                              // cross-origin (OCR): straight to network
});
