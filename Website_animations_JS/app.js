const balloon = document.getElementById('air-balloon')
const cloudOne = document.getElementById('cloud-one')
const cloudTwo = document.getElementById('cloud-two')
const cloudThree = document.getElementById('cloud-three')
const cloudFour = document.getElementById('cloud-four')
const cloudFive = document.getElementById('cloud-five')
const imageOne = document.getElementById('image1')
const imageTwo = document.getElementById('image2')
const imageThree = document.getElementById('image3')

function move() {
    const incrementer = window.scrollY

    // The number refers to the height from the bottom of the sky section
    balloon.style.bottom = 10 + incrementer * 0.1 + '%'

    cloudOne.style.bottom = 40 + incrementer * 0.12 + '%'
    cloudOne.style.left = 75 + incrementer * 0.1 + '%'

    cloudTwo.style.bottom = 80 + incrementer * 0.14 + '%'
    cloudTwo.style.left = 70 + incrementer * 0.15 + '%'

    cloudThree.style.bottom = 60 + incrementer * 0.1 + '%'
    cloudThree.style.left = 0 + incrementer * -0.12 + '%'

    cloudFour.style.bottom = 70 + incrementer * 0.16 + '%'
    cloudFour.style.left = 20 + incrementer * -0.15 + '%'

    cloudFive.style.bottom = 60 + incrementer * 0.2 + '%'
    cloudFive.style.left = 60 + incrementer * 0.16 + '%'

    imageOne.style.left = 20 + incrementer * -2.2 + '%'
    imageTwo.style.left = 26 + incrementer * -1.5 + '%'
    imageThree.style.left = 32 + incrementer * -1 + '%'
}

window.addEventListener('scroll', move)