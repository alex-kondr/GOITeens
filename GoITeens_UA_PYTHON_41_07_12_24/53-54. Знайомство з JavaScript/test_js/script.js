const button = document.getElementById("changeColorButton")
let count = 0
const pElement = document.getElementById("p-element")
const startText = pElement.innerText


pElement.addEventListener("mouseover", function () {
  pElement.innerText = "Ви навели курсор"
});


pElement.addEventListener("mouseout", function () {
  pElement.innerText = "Ви прибрали курсор"
});


pElement.addEventListener("click", function () {
  pElement.innerText = "Ви мене жмакаєте!!!(((("
});


button.addEventListener("click", function () {
  const randomColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
  document.body.style.backgroundColor = randomColor;
  count++
  button.innerText = `Натисли ${count} р.`
  pElement.innerText = startText
});


const firstNumber = document.getElementById("firstNumber")
const secondNumber = document.getElementById("secondNumber")
const resultDiv = document.getElementById("result-div")
const resultSumm = document.getElementById("result-summ")
const resultDivDiv = document.getElementById("result-div//")
const divResultDiv = document.getElementById("result-div%")

const result = document.getElementById("result")

const divNumber = (a, b) => a / b;
const summNumber = (a, b) => a + b;
const divdivNumber = (a, b) => a / b | 0;
const divNumberdiv = (a, b) => a % b;


result.addEventListener("click", function () {
  let a = parseInt(firstNumber.value)
  let b = parseInt(secondNumber.value)
  resultDiv.innerText = `${a} / ${b} = ${divNumber(a, b)}`
  resultSumm.innerText = `${a} + ${b} = ${summNumber(a, b)}`
  resultDivDiv.innerText = `${a} // ${b} = ${divdivNumber(a, b)} - ділення націло`
  divResultDiv.innerText = `${a} % ${b} = ${divNumberdiv(a, b)} - залишок від ділення`
})
