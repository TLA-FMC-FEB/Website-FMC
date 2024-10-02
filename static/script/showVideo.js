const content = document.querySelector(".content");

function showVideo(video) {
    if (video === 'konsepipo') {
        content.innerHTML = `
            <lite-youtube videoid="fpLwzsZPx5A" playlabel="Konsep IPO"></lite-youtube>
        `;
        // videoContent = document.createElement('lite-youtube');
        // videoContent.setAttribute('videoid', 'ogfYd705cRs');
        // videoContent.setAttribute('playlabel', 'Keynote');
        // content.appendChild(videoContent);
    } else if (video === 'pasarmodal') {
        content.innerHTML = `
            <lite-youtube videoid="4sP-PC8O6SI" playlabel="Pasar Modal"></lite-youtube>
        `;
    } else if (video === 'fungsisaham')
        content.innerHTML =`
            <lite-youtube videoid="VP6VbXMDRWU" playlabel="Fungsi Saham"></lite-youtube>
        `;
}