// Detect browser language and set django_language cookie if not present
(function () {
  try {
    if (document.cookie.indexOf('django_language=') === -1) {
      var lang = navigator.language || navigator.userLanguage || 'en-US';
      // Normalize to lowercase-underscore format Django expects sometimes: en-us
      lang = lang.toLowerCase();
      // Only set if different from default html lang
      var htmlLang = document.documentElement.lang || '';
      if (!htmlLang || htmlLang.toLowerCase() !== lang) {
        var cookie = 'django_language=' + encodeURIComponent(lang) + ';path=/';
        // Set a long-lived cookie (30 days)
        var expires = new Date();
        expires.setTime(expires.getTime() + 30 * 24 * 60 * 60 * 1000);
        cookie += ';expires=' + expires.toUTCString();
        document.cookie = cookie;
        // Optionally reload to apply translations on first visit
        try {
          window.location.reload();
        } catch (e) {
          // ignore reload failures
        }
      }
    }
  } catch (e) {
    // Avoid breaking the page if navigator is undefined
    console.error('locale detection failed', e);
  }
})();