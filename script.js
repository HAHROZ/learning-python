// ===============================
// Open / Close Chapters
// ===============================

const toggles = document.querySelectorAll(".toggle");
const search = document.getElementById("search");
const lessons = document.querySelectorAll(".lesson");
const menuToggle = document.getElementById("menu-toggle");
const siteNav = document.getElementById("site-nav");
const moduleToggles = document.querySelectorAll(".module-toggle");

// ===============================
// Site Theme and Language
// ===============================

const themeToggle = document.getElementById("theme-toggle");
const languageToggle = document.getElementById("language-toggle");
let isArabic = true;

const arabicText = {
    "My Course": "دورة بايثون",
    "Learn Programming with Python": "تعلّم البرمجة بلغة Python",
    "Chapter 1": "الفصل الأول",
    "Chapter 2": "الفصل الثاني",
    "Video Lesson": "درس فيديو",
    "Quiz": "اختبار",
    "Multimedia Lesson": "درس وسائط متعددة",
    "Text Lesson": "درس نصي",
    "Survey": "استبيان",
    "PDF Lesson": "درس PDF",
    "Audio Lesson": "درس صوتي",
    "Download Lesson": "درس للتحميل",
    "Presentation Lesson": "درس عرض تقديمي",
    "Assignment Lesson": "واجب",
    "Exam": "اختبار نهائي"
};

const arabicLessonMeta = {
    "VIDEO · 1 MIN": "فيديو · دقيقة واحدة",
    "QUIZ · 4 QUESTIONS": "اختبار · 4 أسئلة",
    "MULTIMEDIA": "وسائط متعددة",
    "TEXT": "نص",
    "SURVEY · 3 QUESTIONS": "استبيان · 3 أسئلة",
    "PDF": "ملف PDF",
    "AUDIO": "صوتي",
    "DOWNLOAD": "تحميل",
    "PRESENTATION": "عرض تقديمي",
    "ASSIGNMENT": "واجب",
    "EXAM": "اختبار نهائي"
};

function applyLanguage() {
    document.documentElement.lang = isArabic ? "ar" : "en";
    document.documentElement.dir = isArabic ? "rtl" : "ltr";
    document.title = isArabic ? "دورة بايثون" : "Learning Python";
    languageToggle.textContent = isArabic ? "English" : "العربية";

    document.querySelectorAll("[data-ar][data-en]").forEach((element) => {
        element.textContent = element.dataset[isArabic ? "ar" : "en"];
    });

    document.querySelectorAll(".course-card h1, .chapter-header h2, .lesson-info h3").forEach((element) => {
        if (element.dataset.ar && element.dataset.en) {
            element.textContent = element.dataset[isArabic ? "ar" : "en"];
            return;
        }
        if (!element.dataset.en) element.dataset.en = element.textContent.trim();
        element.textContent = isArabic ? (arabicText[element.dataset.en] || element.dataset.en) : element.dataset.en;
    });

    document.querySelectorAll(".lesson-info p").forEach((element) => {
        if (!element.dataset.en) element.dataset.en = element.innerHTML;
        if (isArabic) {
            const icon = element.querySelector("i");
            const englishMeta = element.textContent.trim();
            element.innerHTML = `${icon.outerHTML} ${arabicLessonMeta[englishMeta] || englishMeta}`;
        } else {
            element.innerHTML = element.dataset.en;
        }
    });

    search.placeholder = isArabic ? "ابحث بعنوان الدرس" : "Search by lesson title";
}

applyLanguage();

// ===============================
// Mobile Navigation
// ===============================

menuToggle.addEventListener("click", () => {
    const isOpen = siteNav.classList.toggle("open");
    menuToggle.setAttribute("aria-expanded", String(isOpen));
    menuToggle.querySelector("i").className = isOpen
        ? "fa-solid fa-xmark"
        : "fa-solid fa-bars";
});

themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    const isDark = document.body.classList.contains("dark-mode");
    const icon = themeToggle.querySelector("i");

    icon.className = isDark ? "fa-solid fa-sun" : "fa-solid fa-moon";
    themeToggle.querySelector("span").textContent = isDark
        ? (isArabic ? "الوضع الفاتح" : "Light mode")
        : (isArabic ? "الوضع الداكن" : "Dark mode");
});

languageToggle.addEventListener("click", () => {
    isArabic = !isArabic;
    applyLanguage();

    const isDark = document.body.classList.contains("dark-mode");
    themeToggle.querySelector("span").textContent = isDark
        ? (isArabic ? "الوضع الفاتح" : "Light mode")
        : (isArabic ? "الوضع الداكن" : "Dark mode");
});

toggles.forEach((btn) => {
    btn.addEventListener("click", () => {
        const chapter = btn.closest(".chapter");
        const content = chapter.querySelector(".chapter-content");
        const icon = btn.querySelector("i");

        content.classList.toggle("open");

        if (content.classList.contains("open")) {
            icon.classList.remove("fa-chevron-down");
            icon.classList.add("fa-chevron-up");
        } else {
            icon.classList.remove("fa-chevron-up");
            icon.classList.add("fa-chevron-down");
        }
    });
});

// ===============================
// Built-in / Custom Modules
// ===============================

moduleToggles.forEach((button) => {
    button.addEventListener("click", (event) => {
        event.stopPropagation();
        const content = button.closest(".lesson-info").querySelector(".module-content");
        const isOpen = content.classList.toggle("open");

        button.setAttribute("aria-expanded", String(isOpen));
        button.querySelector("i").className = isOpen
            ? "fa-solid fa-chevron-up"
            : "fa-solid fa-chevron-down";
    });
});

// ===============================
// Search Lessons
// ===============================

search.addEventListener("keyup", function () {
    const value = this.value.toLowerCase();

    lessons.forEach((lesson) => {
        const title = lesson.querySelector("h3").textContent.toLowerCase();
        lesson.style.display = title.includes(value) ? "flex" : "none";
    });
});

// ===============================
// Select Active Lesson
// ===============================

lessons.forEach((lesson) => {
    lesson.addEventListener("click", () => {
        document.querySelectorAll(".lesson").forEach((item) => {
            item.classList.remove("active");
        });

        lesson.classList.add("active");
    });
});

// ===============================
// Progress Bar
// ===============================

function updateProgress() {
    const completed = document.querySelectorAll(".lesson.completed").length;
    const total = document.querySelectorAll(".lesson").length;
    const percent = Math.round((completed / total) * 100);

    document.querySelector(".progress").style.width = percent + "%";
    document.querySelector(".course-card p").innerHTML = isArabic
        ? `<strong>${percent}%</strong> مكتمل`
        : `<strong>${percent}%</strong> complete`;
}

updateProgress();

// ===============================
// Toggle Lesson Complete
// ===============================

document.querySelectorAll(".circle").forEach((circle) => {
    circle.addEventListener("click", (event) => {
        event.stopPropagation();

        const lesson = circle.closest(".lesson");
        lesson.classList.toggle("completed");
        circle.classList.toggle("complete");

        circle.innerHTML = circle.classList.contains("complete")
            ? '<i class="fa-solid fa-check"></i>'
            : "";

        updateProgress();
    });
});
