function addCard(){
  var container = document.getElementById("containerfortracks");
  var tracks = document.createElement("div");
  tracks.className = "tracks";
  var img = document.createElement("div");
  img.className = "image";
  var title = document.createElement("h3");
  title.id = "titletracks";
  title.innerHTML = "Title Track";
  var tagcont = document.createElement("div");
  tagcont.id= "tag-container";
  tracks.appendChild(img);
  tracks.appendChild(title);
  tracks.appendChild(tagcont);
  container.appendChild(tracks);
}