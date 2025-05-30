const results = {
    relax: {
        title: "You need a Cozy Throw Pillow!",
        desc: "You love comfort and relaxation. Our soft, earth-toned throw pillows will make your space extra inviting.",
        img: "https://cdn-images.article.com/products/SKU23589/2890x1500/image149309.jpg?w=320&q=80&fit=max",
        link: "throwpillow.html"
    },
    nature: {
        title: "You need a Green Timberline Candle!",
        desc: "Nature inspires you. Our Green Timberline Candle brings the outdoors in with a fresh, calming scent and a beautiful natural look.",
        img: "https://cdn.shoplightspeed.com/shops/628145/files/40851698/hyoola-green-timberline-wood-pillar-candle-2-sizes.jpg",
        link: "candle.html"
    },
    host: {
        title: "You need a Bosmarlin Ceramic Coffee Mug Set!",
        desc: "You love to host and connect. Our Bosmarlin ceramic mug set is perfect for sharing coffee or tea with friends in style.",
        img: "https://m.media-amazon.com/images/I/61MbbXesUxL._AC_UF1000,1000_QL80_.jpg",
        link: "mug.html"
    },
    creative: {
        title: "You need a Tree Bookshelf!",
        desc: "You’re creative and bold. Our tree bookshelf is perfect for displaying your favorite books and art in a unique way.",
        img: "https://m.media-amazon.com/images/I/71pr1F0VWRL._AC_UF894,1000_QL80_.jpg",
        link: "shelf.html"
    },
    bamboo_comforter: {
        title: "You need Bamboo Comforters!",
        desc: "Experience ultimate comfort and eco-friendly luxury with our bamboo comforters, perfect for a restful night's sleep.",
        img: "https://m.media-amazon.com/images/I/81kYqwqRK5L.jpg",
        link: "bamboo-comforter.html"
    },
    avocado_lamp: {
        title: "You need a Linen Avocado Lamp!",
        desc: "Brighten your space with a linen avocado lamp, blending playful design and soft green hues for a cozy vibe.",
        img: "https://i.etsystatic.com/13498126/r/il/f51e55/5960004560/il_570xN.5960004560_ogkm.jpg",
        link: "avocado-lamp.html"
    },
    green_ottoman: {
        title: "You need a Green Storage Ottoman!",
        desc: "Add style and function to your room with a green storage ottoman—perfect for extra seating and hidden storage.",
        img: "https://m.media-amazon.com/images/I/91Akw8ptmmL.jpg",
        link: "green-ottoman.html"
    },
    wicker_chair: {
        title: "You need a Modern Wicker Chair!",
        desc: "Relax in style with a modern wicker chair, bringing natural textures and a fresh look to your home.",
        img: "https://m.media-amazon.com/images/I/A1RVH9JfMwL._AC_UF894,1000_QL80_.jpg",
        link: "wicker-chair.html"
    },
    sage_curtains: {
        title: "You need Sage Green Window Curtains!",
        desc: "Soften your space and add a touch of color with our sage green window curtains, perfect for any room.",
        img: "https://m.media-amazon.com/images/I/71dx4WSLSzL._AC_UF894,1000_QL80_.jpg",
        link: "sage-curtains.html"
    },
    sage_clock: {
        title: "You need a Sage Green Clock!",
        desc: "Keep time in style with a sage green clock, a subtle and elegant accent for your wall.",
        img: "https://i.etsystatic.com/41004641/r/il/868b69/5115136397/il_fullxfull.5115136397_gmsc.jpg",
        link: "sage-clock.html"
    },
    vineyard_side_table: {
        title: "You need a Sage Green Vineyard Side Table!",
        desc: "Bring vineyard charm to your home with this sage green side table, perfect for your favorite book or drink.",
        img: "https://linqcdn.avbportal.com/images/9465fc29-5233-4f83-b54a-8a98e3d57848.jpg?w=160",
        link: "vineyard-side-table.html"
    },
    watercolor_painting: {
        title: "You need a Green Watercolor Abstract Wall Painting!",
        desc: "Add a splash of art to your walls with a green watercolor abstract painting, bringing calm and creativity to your space.",
        img: "https://papermoonartdesign.com/cdn/shop/products/WA232-watercolor-abstract-nature-botanical-green-aesthetic-printable-wall-art-03.jpg?v=1622491445&width=1445",
        link: "watercolor-painting.html"
    },
    vineyard_coffee_table: {
        title: "You need a Sage Green Vineyard Coffee Table!",
        desc: "Complete your living room with a sage green vineyard coffee table, blending rustic charm and modern style.",
        img: "https://linqcdn.avbportal.com/images/3e893a30-252f-4a24-9a8c-f2ebe91ef076.jpg?w=640",
        link: "vineyard-coffee-table.html"
    }
};

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('quizForm');
    const resultDiv = document.getElementById('quizResult');

    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Collect answers
        const answers = {};
        for (let i = 1; i <= 5; i++) {
            const q = form.querySelector(`input[name="q${i}"]:checked`);
            if (q) answers[`q${i}`] = q.value;
        }

        // Tally results
        const tally = { relax: 0, nature: 0, host: 0, creative: 0 };
        Object.values(answers).forEach(val => { 
            if (tally.hasOwnProperty(val)) tally[val]++; 
        });

        // Find all types with the highest count (handle ties)
        const maxCount = Math.max(...Object.values(tally));
        const topTypes = Object.keys(tally).filter(type => tally[type] === maxCount && maxCount > 0);

        // Pick randomly among top types if tie, or fallback to relax
        let maxType = topTypes.length > 0 ? topTypes[Math.floor(Math.random() * topTypes.length)] : 'relax';

        // Result content
        const res = results[maxType];
        if (res) {
            resultDiv.innerHTML = `
                <h2>${res.title}</h2>
                <p>${res.desc}</p>
                <a href="${res.link}" target="_blank" style="display:inline-block;margin:12px 0;">
                    <img src="${res.img}" alt="${res.title}" style="max-width:180px;border-radius:10px;">
                </a>
                <br>
                <a href="${res.link}" target="_blank">
                    <button type="button">See Product</button>
                </a>
            `;
        } else {
            resultDiv.innerHTML = `<p>Sorry, we couldn't determine your result. Please try again.</p>`;
        }
        resultDiv.style.display = 'block';
        resultDiv.scrollIntoView({ behavior: 'smooth' });
    });
});
