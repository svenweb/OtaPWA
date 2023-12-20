// Register the service worker
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
      navigator.serviceWorker.register('/static/js/service-worker.js');
    });
  }
  
  // Install the service worker
  self.addEventListener('install', function(event) {
    event.waitUntil(
      caches.open('my-pwa-cache').then(function(cache) {
        return cache.addAll([
          '/',
          '/static/css/style.css',
          '/static/js/app.js',
          '/static/images/icon-192x192.png',
          '/static/images/icon-512x512.png'
        ]);
      })
    );
  });
  
  // Fetch from the cache
  self.addEventListener('fetch', function(event) {
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
  });