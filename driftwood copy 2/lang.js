const translations = {
  en: {
    "nav-home": "Home",
    "nav-shop": "Shop",
    "nav-about": "About",
    "nav-faq": "FAQ",
    "nav-contact": "Contact",
    "nav-cart": "Cart",
    "newsletter-btn": "Sign up for our newsletter",
    "title-main": "Driftwood Home Decor",
    "desc-main": "Driftwood Home Decor is a curated home and lifestyle brand offering timeless, nature-inspired pieces that bring warmth, calm, and character into every space. From earthy ceramics to soft textiles and handcrafted decor, Driftwood blends organic materials with minimalist design — helping you create a home that feels as beautiful as it is grounded.",
    "quiz-btn-label": "Take the Personality Quiz",
    "team-title": "Our Team",
    "emp1-name": "Jade",
    "emp1-role": "Lead Stylist",
    "emp1-desc": "Creates unique, nature-inspired looks and guides our design vision.",
    "emp2-name": "James",
    "emp2-role": "Customer Experience",
    "emp2-desc": "Ensures every guest feels welcome and helps with all inquiries.",
    "emp3-name": "Maya",
    "emp3-role": "Shop Manager",
    "emp3-desc": "Keeps the shop running smoothly and manages daily operations.",
    "emp4-name": "Lila",
    "emp4-role": "Florist & Decorator",
    "emp4-desc": "Arranges flowers and decor to bring warmth and beauty to every space.",
    "emp5-name": "Eli",
    "emp5-role": "Creative Director",
    "emp5-desc": "Leads branding and creative projects, ensuring a cohesive style.",
    "footer-contact": "hello@driftwooddecor.com"
  },
  es: {
    "nav-home": "Inicio",
    "nav-shop": "Tienda",
    "nav-about": "Acerca de",
    "nav-faq": "Preguntas",
    "nav-contact": "Contacto",
    "nav-cart": "Carrito",
    "newsletter-btn": "Suscríbete a nuestro boletín",
    "title-main": "Decoración para el Hogar Driftwood",
    "desc-main": "Driftwood Home Decor es una marca de hogar y estilo de vida cuidadosamente seleccionada que ofrece piezas atemporales inspiradas en la naturaleza, aportando calidez, calma y carácter a cada espacio. Desde cerámicas terrosas hasta textiles suaves y decoración artesanal, Driftwood combina materiales orgánicos con diseño minimalista, ayudándote a crear un hogar tan hermoso como acogedor.",
    "quiz-btn-label": "Haz el Quiz de Personalidad",
    "team-title": "Nuestro Equipo",
    "emp1-name": "Jade",
    "emp1-role": "Estilista Principal",
    "emp1-desc": "Crea looks únicos inspirados en la naturaleza y guía nuestra visión de diseño.",
    "emp2-name": "James",
    "emp2-role": "Atención al Cliente",
    "emp2-desc": "Asegura que cada visitante se sienta bienvenido y ayuda con todas las consultas.",
    "emp3-name": "Maya",
    "emp3-role": "Gerente de Tienda",
    "emp3-desc": "Mantiene la tienda funcionando sin problemas y gestiona las operaciones diarias.",
    "emp4-name": "Lila",
    "emp4-role": "Florista y Decoradora",
    "emp4-desc": "Arregla flores y decoración para aportar calidez y belleza a cada espacio.",
    "emp5-name": "Eli",
    "emp5-role": "Director Creativo",
    "emp5-desc": "Lidera proyectos de marca y creatividad, asegurando un estilo cohesivo.",
    "footer-contact": "hola@driftwooddecor.com"
  }
};

let currentLang = localStorage.getItem('lang') || 'en';

function setLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('lang', lang);
  for (const key in translations[lang]) {
    const el = document.getElementById(key);
    if (el) {
      el.textContent = translations[lang][key];
    }
  }
}

function toggleLanguage() {
  setLanguage(currentLang === 'en' ? 'es' : 'en');
}

// Set language on page load
document.addEventListener('DOMContentLoaded', () => setLanguage(currentLang));
