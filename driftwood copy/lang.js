const translations = {
  en: {
    newsletter_btn: "Sign up for our newsletter",
    brand: "Driftwood",
    nav_home: "Home",
    nav_shop: "Shop",
    nav_about: "About",
    nav_faq: "FAQ",
    nav_contact: "Contact",
    nav_cart: "Cart",
    theme_switch: "Switch Theme",
    lang_switch: "EN/ES/FR",
    main_title: "Driftwood Home Decor",
    main_desc: "Driftwood Home Decor is a curated home and lifestyle brand offering timeless, nature-inspired pieces that bring warmth, calm, and character into every space. From earthy ceramics to soft textiles and handcrafted decor, Driftwood blends organic materials with minimalist design — helping you create a home that feels as beautiful as it is grounded.",
    quiz_btn: "Take the Personality Quiz",
    team_title: "Our Team",
    emp1_name: "Jade",
    emp1_role: "Lead Stylist",
    emp1_desc: "Creates unique, nature-inspired looks and guides our design vision.",
    emp2_name: "James",
    emp2_role: "Customer Experience",
    emp2_desc: "Ensures every guest feels welcome and helps with all inquiries.",
    emp3_name: "Maya",
    emp3_role: "Shop Manager",
    emp3_desc: "Keeps the shop running smoothly and manages daily operations.",
    emp4_name: "Lila",
    emp4_role: "Florist & Decorator",
    emp4_desc: "Arranges flowers and decor to bring warmth and beauty to every space.",
    emp5_name: "Eli",
    emp5_role: "Creative Director",
    emp5_desc: "Leads branding and creative projects, ensuring a cohesive style.",
    spin_btn: "Spin",
    spin_close: "✖ Close",
    footer_contact_label: "Contact us:",
    footer_copyright: "&copy; 2024 Driftwood Home Decor"
  },
  es: {
    newsletter_btn: "Suscríbete a nuestro boletín",
    brand: "Driftwood",
    nav_home: "Inicio",
    nav_shop: "Tienda",
    nav_about: "Acerca de",
    nav_faq: "Preguntas",
    nav_contact: "Contacto",
    nav_cart: "Carrito",
    theme_switch: "Cambiar tema",
    lang_switch: "EN/ES/FR",
    main_title: "Decoración para el Hogar Driftwood",
    main_desc: "Driftwood Home Decor es una marca de hogar y estilo de vida cuidadosamente seleccionada que ofrece piezas atemporales inspiradas en la naturaleza, aportando calidez, calma y carácter a cada espacio. Desde cerámicas terrosas hasta textiles suaves y decoración artesanal, Driftwood combina materiales orgánicos con diseño minimalista, ayudándote a crear un hogar tan hermoso como acogedor.",
    quiz_btn: "Haz el test de personalidad",
    team_title: "Nuestro equipo",
    emp1_name: "Jade",
    emp1_role: "Estilista principal",
    emp1_desc: "Crea looks únicos inspirados en la naturaleza y guía nuestra visión de diseño.",
    emp2_name: "James",
    emp2_role: "Atención al cliente",
    emp2_desc: "Se asegura de que cada cliente se sienta bienvenido y ayuda con todas las consultas.",
    emp3_name: "Maya",
    emp3_role: "Gerente de tienda",
    emp3_desc: "Mantiene la tienda funcionando sin problemas y gestiona las operaciones diarias.",
    emp4_name: "Lila",
    emp4_role: "Florista y decoradora",
    emp4_desc: "Arregla flores y decoración para aportar calidez y belleza a cada espacio.",
    emp5_name: "Eli",
    emp5_role: "Director creativo",
    emp5_desc: "Lidera proyectos creativos y de marca, asegurando un estilo cohesivo.",
    spin_btn: "Girar",
    spin_close: "✖ Cerrar",
    footer_contact_label: "Contáctanos:",
    footer_copyright: "&copy; 2024 Driftwood Home Decor"
  },
  fr: {
    newsletter_btn: "Inscrivez-vous à notre newsletter",
    brand: "Driftwood",
    nav_home: "Accueil",
    nav_shop: "Boutique",
    nav_about: "À propos",
    nav_faq: "FAQ",
    nav_contact: "Contact",
    nav_cart: "Panier",
    theme_switch: "Changer de thème",
    lang_switch: "EN/ES/FR",
    main_title: "Décoration Maison Driftwood",
    main_desc: "Driftwood Home Decor est une marque de maison et de style de vie proposant des pièces intemporelles inspirées de la nature, apportant chaleur et calme à chaque espace. Des céramiques naturelles aux textiles lisses et à la décoration artisanale, Driftwood associe matériaux biologiques et couleurs minimalistes— pour décorer votre maison avec élégance.",
    quiz_btn: "Faire le quiz de personnalité",
    team_title: "Notre équipe",
    emp1_name: "Jade",
    emp1_role: "Styliste principale",
    emp1_desc: "Crée des looks uniques inspirés de la nature et guide notre vision du design.",
    emp2_name: "James",
    emp2_role: "Expérience client",
    emp2_desc: "Veille à ce que chaque client se sente bienvenu et aide pour toutes les demandes.",
    emp3_name: "Maya",
    emp3_role: "Responsable boutique",
    emp3_desc: "Assure le bon fonctionnement de la boutique et gère les opérations quotidiennes.",
    emp4_name: "Lila",
    emp4_role: "Fleuriste & décoratrice",
    emp4_desc: "Compose des fleurs et de la décoration pour apporter chaleur et beauté à chaque espace.",
    emp5_name: "Eli",
    emp5_role: "Directeur créatif",
    emp5_desc: "Dirige les projets créatifs et de branding, assurant un style cohérent.",
    spin_btn: "Tourner",
    spin_close: "✖ Fermer",
    footer_contact_label: "Contactez-nous :",
    footer_copyright: "&copy; 2024 Driftwood Home Decor"
  }
};

let currentLang = "en";
function setLanguage(lang) {
  currentLang = lang;
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (translations[lang][key]) {
      el.innerHTML = translations[lang][key];
    }
  });
}
function toggleLanguage() {
  if (currentLang === "en") setLanguage("es");
  else if (currentLang === "es") setLanguage("fr");
  else setLanguage("en");
}
document.addEventListener("DOMContentLoaded", () => setLanguage(currentLang));
