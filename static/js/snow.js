function createSnowflake() {
    const snowflake = document.createElement('div');
    snowflake.classList.add('snowflake');

    const startLeft = Math.random() * window.innerWidth;
    const duration = Math.random() * 3 + 2;
    const size = Math.random() * 5 + 3;
    const opacity = Math.random() * 1.5 + 0.3;

    snowflake.style.left = startLeft + 'px';
    snowflake.style.width = size + 'px';
    snowflake.style.height = size + 'px';
    snowflake.style.opacity = opacity;
    snowflake.style.animation = `fall ${duration}s linear infinite`;

    document.body.appendChild(snowflake);

    setTimeout(() => {
        snowflake.remove();
    }, duration * 1000);
}

setInterval(createSnowflake, 100);