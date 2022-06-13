function dict(){
    var x = document.getElementById("search").value;
    const url = "https://www.dictionary.com/browse/";
    var url1 = url + x;
    var win = window.open(url1, '_self');
    win.focus;
  }