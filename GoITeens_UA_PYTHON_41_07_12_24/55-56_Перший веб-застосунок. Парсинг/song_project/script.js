const songs = [
    "Imagine Dragons - Believer",
    "Ed Sheeran - Shape of You",
    "Beyoncé - Halo",
    "The Weeknd - Blinding Lights",
    "Coldplay - Viva La Vida",
    "Adele - Rolling in the Deep",
    "Maroon 5 - Sugar",
    "OneRepublic - Counting Stars",
    "Taylor Swift - Shake It Off",
    "Post Malone - Circles",
    "Shawn Mendes - Treat You Better",
    "Justin Bieber - Love Yourself",
    "Dua Lipa - Don't Start Now",
    "Lady Gaga - Shallow",
    "Billie Eilish - Bad Guy",
    "Bruno Mars - Uptown Funk",
    "Harry Styles - Watermelon Sugar",
    "Chainsmokers - Closer",
    "Linkin Park - Numb",
    "Katy Perry - Roar",
    "Sam Smith - Stay With Me"
];

const songName = document.getElementById("song_name");
console.log("songName", songName);
const button = document.getElementById("button");
console.log("button", button);
const result = document.getElementById("result");
console.log("result", result);

button.addEventListener("click", () => {
    console.log("songName.value", songName.value);

    const songIndex = songs.findIndex(song =>
        song.includes(songName.value)
    );
    console.log("songIndex", songIndex);
    if (songIndex === -1) {
        result.textContent = "Такої пісні немає у списку";
    } else {
        result.textContent = `Пісня "${songs[songIndex]}" знайдено під номером ${songIndex + 1}`;
    }
});
