// Keep the first visit aligned with the browser/device language.
(function () {
  try {
    if (document.cookie.indexOf('django_language=') !== -1) {
      return;
    }

    var browserLanguages = navigator.languages || [navigator.language || navigator.userLanguage];
    var language = 'en-us';
    for (var i = 0; i < browserLanguages.length; i += 1) {
      var primaryLanguage = (browserLanguages[i] || '').toLowerCase().split('-')[0];
      if (primaryLanguage === 'fr') {
        language = 'fr-fr';
        break;
      }
      if (primaryLanguage === 'pt') {
        language = 'pt-br';
        break;
      }
      if (primaryLanguage === 'en') {
        language = 'en-us';
        break;
      }
    }

    var htmlLanguage = (document.documentElement.lang || '').toLowerCase();
    if (htmlLanguage !== language) {
      var cookie = 'django_language=' + encodeURIComponent(language) + ';path=/;samesite=lax';
      var expires = new Date();
      expires.setTime(expires.getTime() + 365 * 24 * 60 * 60 * 1000);
      document.cookie = cookie + ';expires=' + expires.toUTCString();
      window.location.reload();
    }
  } catch (e) {
    // Language detection must never prevent the application from loading.
  }
})();
