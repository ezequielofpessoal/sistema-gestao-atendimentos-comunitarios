// Máscara automática de CPF para a Tela 2 (Formulário de Cadastro)
document.addEventListener("DOMContentLoaded", function() {
    const cpfInput = document.getElementById("cpf");
    
    if (cpfInput) {
        cpfInput.addEventListener("input", function (e) {
            let value = e.target.value.replace(/\D/g, ""); // Remove tudo que não é dígito
            
            if (value.length > 11) {
                value = value.slice(0, 11);
            }
            
            // Aplica a formatação 000.000.000-00
            if (value.length > 9) {
                value = value.replace(/^(\d{3})(\d{3})(\d{3})(\d{2}).*/, "$1.$2.$3-$4");
            } else if (value.length > 6) {
                value = value.replace(/^(\d{3})(\d{3})(\d{1,3}).*/, "$1.$2.$3");
            } else if (value.length > 3) {
                value = value.replace(/^(\d{3})(\d{1,3}).*/, "$1.$2");
            }
            
            e.target.value = value;
        });
    }
});
