function addCard(){
  var container = document.getElementById("containerfortracks");
  var tracks = document.createElement("div");
  tracks.className = "tracks";
  var img = document.createElement("div");
  img.id = "image";
  var title = document.createElement("h3");
  title.id = "tracktitles";
  title.innerHTML = "Title Track";
  var tagcont = document.createElement("div");
  tagcont.id= "tag-container";
  var tagbox = document.createElement("div");
  tagbox.id = "tags";
  var tag = document.createElement("p");
  tag.innerHTML = "Chill";
  tag.id = "tag-labels";
  tagbox.appendChild(tag);
  tagcont.appendChild(tagbox);
  tracks.appendChild(img);
  tracks.appendChild(title);
  tracks.appendChild(tagcont);
  container.appendChild(tracks);
}
