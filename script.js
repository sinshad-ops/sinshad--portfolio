document.addEventListener('DOMContentLoaded', () => {
  // ==========================================
  // 1. Custom Interactive Cursor Follower (with LERP)
  // ==========================================
  const cursorDot = document.querySelector('.custom-cursor');
  const cursorFollower = document.querySelector('.custom-cursor-follower');
  const cursorGlow = document.querySelector('.custom-cursor-glow');

  let mouseX = 0, mouseY = 0; // Actual mouse position
  let followerX = 0, followerY = 0; // Interpolated follower position

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;

    // Direct update for dot and glow (immediate)
    if (cursorDot) {
      cursorDot.style.left = `${mouseX}px`;
      cursorDot.style.top = `${mouseY}px`;
    }
    if (cursorGlow) {
      cursorGlow.style.left = `${mouseX}px`;
      cursorGlow.style.top = `${mouseY}px`;
    }
  });

  // LERP Loop for smooth lag-chase ring follower
  function updateFollower() {
    // Lerp formula: current + (target - current) * factor
    followerX += (mouseX - followerX) * 0.15;
    followerY += (mouseY - followerY) * 0.15;

    if (cursorFollower) {
      cursorFollower.style.left = `${followerX}px`;
      cursorFollower.style.top = `${followerY}px`;
    }
    requestAnimationFrame(updateFollower);
  }
  updateFollower();

  // Add Hover Scaling Classes to Cursor
  const hoverElements = document.querySelectorAll('a, button, .project-card, .contact-card, .theme-toggle-btn');
  hoverElements.forEach(el => {
    el.addEventListener('mouseenter', () => document.body.classList.add('hovering-link'));
    el.addEventListener('mouseleave', () => document.body.classList.remove('hovering-link'));
  });


  // ==========================================
  // 2. Cosmic Engine (Stars, Nebulae & Shooting Stars)
  // ==========================================
  const canvas = document.getElementById('bg-canvas');
  const ctx = canvas.getContext('2d');

  let width = canvas.width = window.innerWidth;
  let height = canvas.height = window.innerHeight;

  const particles = [];
  const shootingStars = [];
  const nebulae = [];
  const starCount = Math.min(120, Math.floor((width * height) / 13000));

  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  // Nebula Clouds (Slow drifting glow spheres)
  class Nebula {
    constructor() {
      this.reset();
      this.x = Math.random() * width;
      this.y = Math.random() * height;
    }
    reset() {
      this.radius = Math.random() * 250 + 200;
      this.x = Math.random() > 0.5 ? -this.radius : width + this.radius;
      this.y = Math.random() * height;
      this.speedX = (Math.random() * 0.15 + 0.05) * (Math.random() > 0.5 ? 1 : -1);
      this.speedY = (Math.random() * 0.1 + 0.05) * (Math.random() > 0.5 ? 1 : -1);
      this.color = Math.random() > 0.5 ? '0, 242, 254' : '157, 78, 221'; // Cyan or Purple
      this.alpha = Math.random() * 0.04 + 0.02;
    }
    update() {
      this.x += this.speedX;
      this.y += this.speedY;

      // Reset when drift completely out of bounds
      if (this.x < -this.radius || this.x > width + this.radius || this.y < -this.radius || this.y > height + this.radius) {
        this.reset();
      }
    }
    draw() {
      const grad = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, this.radius);
      grad.addColorStop(0, `rgba(${this.color}, ${this.alpha})`);
      grad.addColorStop(0.5, `rgba(${this.color}, ${this.alpha * 0.4})`);
      grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
      
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  // Floating Star Particle
  class Particle {
    constructor() {
      this.reset();
      this.y = Math.random() * height;
    }
    reset() {
      this.x = Math.random() * width;
      this.y = 0;
      this.size = Math.random() * 1.8 + 0.4;
      this.speedY = Math.random() * 0.35 + 0.08;
      this.speedX = (Math.random() - 0.5) * 0.15;
      this.alpha = Math.random() * 0.6 + 0.2;
      this.color = Math.random() > 0.6 ? '0, 242, 254' : '157, 78, 221';
    }
    update() {
      this.y += this.speedY;
      this.x += this.speedX;

      // Wrap horizontal
      if (this.x < 0) this.x = width;
      if (this.x > width) this.x = 0;

      // Reset on bottom out
      if (this.y > height) this.reset();

      // Mouse attraction pull
      if (mouseX && mouseY) {
        const dx = this.x - mouseX;
        const dy = this.y - mouseY;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 180) {
          const force = (180 - dist) / 180;
          this.x -= (dx / dist) * force * 0.8;
          this.y -= (dy / dist) * force * 0.8;
        }
      }
    }
    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${this.color}, ${this.alpha})`;
      ctx.fill();
    }
  }

  // Shooting Star Particle
  class ShootingStar {
    constructor() {
      this.reset();
    }
    reset() {
      this.x = Math.random() * width;
      this.y = Math.random() * (height / 2);
      this.length = Math.random() * 80 + 50;
      this.speed = Math.random() * 8 + 4;
      this.angle = Math.PI / 6 + (Math.random() * 0.1); // Spawns falling diagonal right
      this.dx = Math.cos(this.angle) * this.speed;
      this.dy = Math.sin(this.angle) * this.speed;
      this.alpha = 1;
      this.fade = Math.random() * 0.015 + 0.01;
    }
    update() {
      this.x += this.dx;
      this.y += this.dy;
      this.alpha -= this.fade;
    }
    draw() {
      if (this.alpha <= 0) return;
      ctx.strokeStyle = `rgba(0, 242, 254, ${this.alpha})`;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(this.x, this.y);
      ctx.lineTo(this.x - this.dx * 1.5, this.y - this.dy * 1.5);
      ctx.stroke();
    }
  }

  // Populate Cosmic entities
  for (let i = 0; i < 3; i++) nebulae.push(new Nebula());
  for (let i = 0; i < starCount; i++) particles.push(new Particle());

  // Loop rendering
  function renderUniverse() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.06)'; // Creates a trailing glow behind shooting stars
    ctx.clearRect(0, 0, width, height);

    // Drifting Nebulae
    nebulae.forEach(nebula => {
      nebula.update();
      nebula.draw();
    });

    // Starfield particles
    particles.forEach(star => {
      star.update();
      star.draw();
    });

    // Periodically spawn shooting star
    if (Math.random() < 0.003 && shootingStars.length < 2) {
      shootingStars.push(new ShootingStar());
    }

    shootingStars.forEach((star, index) => {
      star.update();
      star.draw();
      if (star.alpha <= 0) {
        shootingStars.splice(index, 1);
      }
    });

    requestAnimationFrame(renderUniverse);
  }
  renderUniverse();


  // ==========================================
  // 3. 3D Parallax Card Tilt Mechanics
  // ==========================================
  const tiltCards = document.querySelectorAll('[data-tilt]');

  tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left; // Mouse relative X inside card
      const y = e.clientY - rect.top;  // Mouse relative Y inside card

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      // Rotation bounds max 12 degrees
      const rotateX = ((centerY - y) / centerY) * 12;
      const rotateY = ((x - centerX) / centerX) * 12;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
    });
  });


  // ==========================================
  // 4. Premium Magnetic Button Interaction
  // ==========================================
  const magneticButtons = document.querySelectorAll('.btn');

  magneticButtons.forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2; // Offset from center
      const y = e.clientY - rect.top - rect.height / 2;

      // Translate button by 35% of offset, creating dynamic magnet pull
      btn.style.transform = `translate(${x * 0.35}px, ${y * 0.35}px) scale(1.03)`;
    });

    btn.addEventListener('mouseleave', () => {
      btn.style.transform = 'translate(0px, 0px) scale(1)';
    });
  });


  // ==========================================
  // 5. Light/Dark Celestial Theme Toggle
  // ==========================================
  const themeToggleBtn = document.querySelector('.theme-toggle-btn');
  const toggleIcon = themeToggleBtn.querySelector('i');

  // Check saved localStorage theme
  const currentTheme = localStorage.getItem('theme');
  if (currentTheme === 'light') {
    document.body.classList.add('light-theme');
    toggleIcon.className = 'fas fa-moon';
  } else {
    toggleIcon.className = 'fas fa-sun';
  }

  themeToggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('light-theme');
    const isLight = document.body.classList.contains('light-theme');

    if (isLight) {
      toggleIcon.className = 'fas fa-moon';
      localStorage.setItem('theme', 'light');
    } else {
      toggleIcon.className = 'fas fa-sun';
      localStorage.setItem('theme', 'dark');
    }
  });


  // ==========================================
  // 6. Typing Tagline Animation
  // ==========================================
  const typedTextSpan = document.querySelector(".typed-text");
  const roles = ["Python Developer", "Web Developer", "Gamer"];
  const typingSpeed = 100;
  const erasingSpeed = 60;
  const newWordDelay = 2200;
  let roleIndex = 0;
  let charIndex = 0;

  function type() {
    if (charIndex < roles[roleIndex].length) {
      typedTextSpan.textContent += roles[roleIndex].charAt(charIndex);
      charIndex++;
      setTimeout(type, typingSpeed);
    } else {
      setTimeout(erase, newWordDelay);
    }
  }

  function erase() {
    if (charIndex > 0) {
      typedTextSpan.textContent = roles[roleIndex].substring(0, charIndex - 1);
      charIndex--;
      setTimeout(erase, erasingSpeed);
    } else {
      roleIndex = (roleIndex + 1) % roles.length;
      setTimeout(type, typingSpeed + 500);
    }
  }

  if (typedTextSpan) {
    setTimeout(type, 1000);
  }


  // ==========================================
  // 7. Navigation Shadow, Back to Top, and Mobile Drawer
  // ==========================================
  const header = document.querySelector('header');
  const backToTop = document.querySelector('.back-to-top');
  const menuBtn = document.querySelector('.menu-btn');
  const nav = document.querySelector('nav');
  const navLinks = document.querySelectorAll('nav a');

  window.addEventListener('scroll', () => {
    // Header scrolled state
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    // Back to top indicator
    if (window.scrollY > 500) {
      backToTop.classList.add('active');
    } else {
      backToTop.classList.remove('active');
    }
  });

  menuBtn.addEventListener('click', () => {
    nav.classList.toggle('active');
    const icon = menuBtn.querySelector('i');
    if (nav.classList.contains('active')) {
      icon.className = 'fas fa-times';
    } else {
      icon.className = 'fas fa-bars';
    }
  });

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('active');
      menuBtn.querySelector('i').className = 'fas fa-bars';
    });
  });


  // ==========================================
  // 8. Intersection Observer for Scroll Reveals & Skills Animation
  // ==========================================
  const revealElements = document.querySelectorAll('.reveal');
  const sections = document.querySelectorAll('section');
  const skillBars = document.querySelectorAll('.skill-bar-inner');

  const observerOptions = {
    root: null,
    threshold: 0.12,
    rootMargin: '0px'
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        
        // Trigger skills progress filling
        if (entry.target.id === 'skills') {
          skillBars.forEach(bar => {
            const percent = bar.getAttribute('data-percent');
            bar.style.width = percent + '%';
          });
        }
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  revealElements.forEach(el => revealObserver.observe(el));
  const skillsSection = document.getElementById('skills');
  if (skillsSection) revealObserver.observe(skillsSection);

  // Active Nav Tracker on Scroll
  window.addEventListener('scroll', () => {
    let currentSection = '';

    sections.forEach(section => {
      const sectionTop = section.offsetTop - 150;
      const sectionHeight = section.clientHeight;
      if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
        currentSection = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href').slice(1) === currentSection) {
        link.classList.add('active');
      }
    });
  });


  // ==========================================
  // 9. Contact Form submission logic
  // ==========================================
  const contactForm = document.getElementById('contact-form');
  const formStatus = document.querySelector('.form-status');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const btn = contactForm.querySelector('button');
      const originalText = btn.innerHTML;
      btn.disabled = true;
      btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Initializing Transmission...';

      setTimeout(() => {
        btn.disabled = false;
        btn.innerHTML = originalText;
        contactForm.reset();

        formStatus.className = 'form-status success';
        formStatus.innerHTML = '<i class="fas fa-check-circle"></i> Message broadcasted successfully! Sinshad will respond shortly.';
        
        setTimeout(() => {
          formStatus.style.display = 'none';
        }, 5000);
      }, 1800);
    });
  }
});
