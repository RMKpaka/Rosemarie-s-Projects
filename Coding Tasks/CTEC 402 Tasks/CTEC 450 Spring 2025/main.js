/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
    navToggle = document.getElementById('nav-toggle'),
    navClose = document.getElementById('nav-close');

if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show-menu');
    });
}

if (navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show-menu');
    });
}

/*=============== REMOVE MENU MOBILE ===============*/
const navLink = document.querySelectorAll('.nav__link');
const linkAction = () => {
    navMenu.classList.remove('show-menu');
};
navLink.forEach(n => n.addEventListener('click', linkAction));

/*=============== SHADOW HEADER ===============*/
const shadowHeader = () => {
    const header = document.getElementById('header');
    this.scrollY >= 50 ? header.classList.add('shadow-header') : header.classList.remove('shadow-header');
};
window.addEventListener('scroll', shadowHeader);

/*=============== EMAIL FORM SUBMISSION ===============*/
const contactForm = document.getElementById('contact-form'),
    contactMessage = document.getElementById('contact-message');

const sendEmail = (e) => {
    e.preventDefault();
    emailjs.sendForm('your_service_id', 'your_template_id', '#contact-form', 'your_public_key')
        .then(() => {
            contactMessage.textContent = "Message sent successfully ✅";
            contactMessage.style.color = "green";
            setTimeout(() => { contactMessage.textContent = ''; }, 5000);
            contactForm.reset();
        })
        .catch((error) => {
            contactMessage.textContent = "Message not sent ❌";
            contactMessage.style.color = "red";
        });
};
contactForm.addEventListener('submit', sendEmail);

/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 400
});

sr.reveal(`.home__name, .home__description, .about__info, .projects__title, .contact__title`, { origin: 'left' });
sr.reveal(`.home__social, .about__image, .projects__list, .contact__form`, { origin: 'right' });

/*=============== CHATBOT FUNCTIONALITY ===============*/
document.addEventListener("DOMContentLoaded", function () {
    let chatbotHeader = document.getElementById("chatbot-header");
    let chatbotBox = document.getElementById("chatbot-box");
    let chatbotMessages = document.getElementById("chatbot-messages");
    let inputField = document.getElementById("chatbot-input");
    let sendButton = document.getElementById("chatbot-send");

    chatbotHeader.addEventListener("click", function () {
        chatbotBox.style.display = chatbotBox.style.display === "block" ? "none" : "block";
    });

    function getChatbotResponse(userMessage) {
        let lowerCaseMessage = userMessage.toLowerCase();
        if (lowerCaseMessage.includes("hello") || lowerCaseMessage.includes("hi")) {
            return "Hi there! I'm Rosemarie's chatbot. How can I assist you today?";
        } else if (lowerCaseMessage.includes("your name")) {
            return "I'm Rosemarie's chatbot, here to help with portfolio inquiries!";
        } else if (lowerCaseMessage.includes("skills")) {
            return "Rosemarie specializes in cybersecurity, IT support, and network security.";
        } else if (lowerCaseMessage.includes("projects")) {
            return "Rosemarie has worked on Cybersecurity Risk Assessment and IT Automation. Check the Projects section!";
        } else if (lowerCaseMessage.includes("resume")) {
            return "You can download Rosemarie's resume from the Resume section.";
        } else if (lowerCaseMessage.includes("contact")) {
            return "Use the Contact section to send Rosemarie a message.";
        } else {
            return "I'm not sure I understand. Can you try rephrasing your question?";
        }
    }

    function sendChatMessage() {
        let userMessage = inputField.value.trim();
        if (userMessage === "") return;
        let userMessageElement = document.createElement("p");
        userMessageElement.innerHTML = `<strong>You:</strong> ${userMessage}`;
        chatbotMessages.appendChild(userMessageElement);
        inputField.value = "";
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
        setTimeout(() => {
            let botReply = getChatbotResponse(userMessage);
            let botMessageElement = document.createElement("p");
            botMessageElement.innerHTML = `<strong>Bot:</strong> ${botReply}`;
            chatbotMessages.appendChild(botMessageElement);
            chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
        }, 500);
    }

    sendButton.addEventListener("click", sendChatMessage);
    inputField.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendChatMessage();
        }
    });
});
