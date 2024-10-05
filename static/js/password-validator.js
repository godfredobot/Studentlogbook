const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirmPassword');
const passwordError = document.getElementById('passwordError');
const confirmPasswordError = document.getElementById('confirmPasswordError');
const submitBtn = document.getElementById('submitBtn');

function validatePassword() {
    const password = passwordInput.value;
    let isValid = true;

    if (password.length < 8) {
        passwordError.textContent = 'Password must be at least 8 characters long';
        isValid = false;
    } else if (!/[A-Z]/.test(password)) {
        passwordError.textContent = 'Password must contain at least one uppercase letter';
        isValid = false;
    } else if (!/[a-z]/.test(password)) {
        passwordError.textContent = 'Password must contain at least one lowercase letter';
        isValid = false;
    } else if (!/[0-9]/.test(password)) {
        passwordError.textContent = 'Password must contain at least one number';
        isValid = false;
    } else if (!/[^A-Za-z0-9]/.test(password)) {
        passwordError.textContent = 'Password must contain at least one special character';
        isValid = false;
    } else {
        passwordError.textContent = '';
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