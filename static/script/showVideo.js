const content = document.querySelector(".content");

function showVideo(video) {
    if (video === 'konsepipo') {
        content.innerHTML = `
            <lite-youtube videoid="fpLwzsZPx5A" playlabel="Konsep IPO"></lite-youtube>
        `;
    } else if (video === 'pasarmodal') {
        content.innerHTML = `
            <lite-youtube videoid="4sP-PC8O6SI" playlabel="Pasar Modal"></lite-youtube>
        `;
    } else if (video === 'klasifikasi') {
        content.innerHTML = `
            <lite-youtube videoid="VP6VbXMDRWU" playlabel="Klasifikasi Perusahaan"></lite-youtube>
        `;
    } else if (video === 'tercatat') {
        content.innerHTML = `
            <lite-youtube videoid="nyrNeW9HJTQ" playlabel="Sektor dan Industri Perusahaan Tercatat di BEI"></lite-youtube>
        `;
    } else if (video === 'istilah') {
        content.innerHTML = `
            <lite-youtube videoid="DPrsKsivvJc" playlabel="Istilah Terkait Dividen"></lite-youtube>
        `;
    } else if (video === 'gorengan') {
        content.innerHTML = `
            <lite-youtube videoid="89O-3hW8e8o" playlabel="Deviden Trap"></lite-youtube>
        `;
    } else if (video === 'obligasi') {
        content.innerHTML = `
            <lite-youtube videoid="OjqmDv4wc-8" playlabel="Konsep Obligasi"></lite-youtube>
        `;
        
    } else if (video === 'jenis') {
        content.innerHTML = `
            <lite-youtube videoid="NO5mPjiMC7U" playlabel="Jenis Obligasi"></lite-youtube>
        `;
    } else if (video === 'assets') {
        content.innerHTML = `
            <lite-youtube videoid="Q1Tg0Nb00hQ" playlabel="Jenis Obligasi"></lite-youtube>
        `;
        
    } else if (video === 'fungsisaham') {
        content.innerHTML =`
            <lite-youtube videoid="VP6VbXMDRWU" playlabel="Fungsi Saham"></lite-youtube>
        `;
    }
}