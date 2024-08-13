document.addEventListener('DOMContentLoaded', function() {
    const cookieBar = document.getElementById('cookie-consent-bar');
    const acceptButton = document.getElementById('cookie-accept');
    const learnMoreLink = document.getElementById('cookie-learn-more');

    function setCookie(name, value, days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();
        document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }

    function getCookie(name) {
        const nameEQ = name + "=";
        const ca = document.cookie.split(';');
        for(let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    function acceptCookies() {
        setCookie('cookie_consent', 'accepted', 365);
        cookieBar.style.display = 'none';
    }

    acceptButton.addEventListener('click', acceptCookies);

    learnMoreLink.addEventListener('click', function(e) {
        e.preventDefault();
        window.location.href = this.getAttribute('href');
    });

    if (getCookie('cookie_consent') !== 'accepted') {
        cookieBar.style.display = 'block';
    }
});