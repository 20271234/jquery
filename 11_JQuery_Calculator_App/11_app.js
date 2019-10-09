// Minus Button
$('#minus-button').click(function() {
   $('#operator').text($(this).text());
   calculate();
});

// Plus Button
$('#plus-button').click(function() {
    $('#operator').text($(this).text());
    calculate();
});

// Divide Button
$('#divide-button').click(function() {
    $('#operator').text($(this).text());
    calculate();
});

// Multiply Button
$('#multiply-button').click(function() {
    $('#operator').text($(this).text());
    calculate();
});

// Calculate
let calculate = () => {
    let firstNumber = $('#firstNumber').val();
    let secondNumber = $('#secondNumber').val();
    let operator = $('#operator').text();
    let result = 0;
    if(firstNumber !== '' && secondNumber !== ''){
        firstNumber = Number(firstNumber);
        secondNumber = Number(secondNumber);
        switch(operator){
            case '+':
                result = firstNumber + secondNumber;
                break;
            case '-':
                result = firstNumber - secondNumber;
                break;
            case '/':
                result = firstNumber / secondNumber;
                break;
            case '*':
                result = firstNumber * secondNumber;
                break;
        }
        $('#result-button').text(result);
    }
};

// Clear Button
$('#clear-button').click(function() {
    $('#firstNumber').val('');
    $('#secondNumber').val('');
    $('#operator').text('+');
    $('#result-button').text('RESET');
});