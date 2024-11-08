const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirmPassword');
const passwordError = document.getElementById('passwordError');
const confirmPasswordError = document.getElementById('confirmPasswordError');
const submitBtn = document.getElementById('submitBtn');

const lengthCriterion = document.getElementById('lengthCriterion');
const uppercaseCriterion = document.getElementById('uppercaseCriterion');
const lowercaseCriterion = document.getElementById('lowercaseCriterion');
const numberCriterion = document.getElementById('numberCriterion');
const specialCharCriterion = document.getElementById('specialCharCriterion');
const strengthMessage = document.getElementById('strengthMessage');

function validatePassword() {
    const password = passwordInput.value;
    let isValid = true;
    let strength = 0;

    // Length check
    if (password.length >= 12) {
        lengthCriterion.classList.remove('text-red-500');
        lengthCriterion.classList.add('text-green-500');
        strength++;
    } else {
        lengthCriterion.classList.add('text-red-500');
        lengthCriterion.classList.remove('text-green-500');
        isValid = false;
    }

    // Uppercase check
    if (/[A-Z]/.test(password)) {
        uppercaseCriterion.classList.remove('text-red-500');
        uppercaseCriterion.classList.add('text-green-500');
        strength++;
    } else {
        uppercaseCriterion.classList.add('text-red-500');
        uppercaseCriterion.classList.remove('text-green-500');
        isValid = false;
    }

    // Lowercase check
    if (/[a-z]/.test(password)) {
        lowercaseCriterion.classList.remove('text-red-500');
        lowercaseCriterion.classList.add('text-green-500');
        strength++;
    } else {
        lowercaseCriterion.classList.add('text-red-500');
        lowercaseCriterion.classList.remove('text-green-500');
        isValid = false;
    }

    // Number check
    if (/[0-9]/.test(password)) {
        numberCriterion.classList.remove('text-red-500');
        numberCriterion.classList.add('text-green-500');
        strength++;
    } else {
        numberCriterion.classList.add('text-red-500');
        numberCriterion.classList.remove('text-green-500');
        isValid = false;
    }

    // Special character check
    if (/[^A-Za-z0-9]/.test(password)) {
        specialCharCriterion.classList.remove('text-red-500');
        specialCharCriterion.classList.add('text-green-500');
        strength++;
    } else {
        specialCharCriterion.classList.add('text-red-500');
        specialCharCriterion.classList.remove('text-green-500');
        isValid = false;
    }

    // Update password strength message
    if (strength <= 2) {
        strengthMessage.textContent = 'Weak';
        strengthMessage.className = 'text-red-500';
    } else if (strength === 3 || strength === 4) {
        strengthMessage.textContent = 'Medium';
        strengthMessage.className = 'text-yellow-500';
    } else if (strength === 5) {
        strengthMessage.textContent = 'Strong';
        strengthMessage.className = 'text-green-500';
    }

    return isValid;
}

function validateConfirmPassword() {
    const password = passwordInput.value;
    const confirmPassword = confirmPasswordInput.value;

    if (password !== confirmPassword) {
        confirmPasswordError.textContent = 'Passwords do not match';
        return false;
    } else {
        confirmPasswordError.textContent = '';
        return true;
    }
}

function updateSubmitButton() {
    submitBtn.disabled = !(validatePassword() && validateConfirmPassword());
}

passwordInput.addEventListener('input', () => {
    validatePassword();
    updateSubmitButton();
});

confirmPasswordInput.addEventListener('input', () => {
    validateConfirmPassword();
    updateSubmitButton();
});
