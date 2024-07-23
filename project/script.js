const imgHeroSection = document.getElementById("photo")
const leftArrow = document.getElementById("img1")
const rightArrow = document.getElementById("img2")

const heroSectionPhotos = [
    "./assets/images.jpeg",
    "./assets/photo1.webp",
    "./assets/photo2.jpg"
]

let index = 0

setInterval(function(){
    index += 1
    if(index >= heroSectionPhotos.length){
        index = 0
    }
    imgHeroSection.src = heroSectionPhotos[index]
    
},5000)




