# my_stie

app.css

@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Open+Sans:wght@400;700&display=swap');

* {
  box-sizing: border-box;
}

html {
  font-family: 'Open Sans', 'Lato', sans-serif;
}

body {
  margin: 0;
}

h1,
h2,
h3 {
  font-family: 'Lato', sans-serif;
  font-weight: bold;
}

#main-navigation {
  width: 100%;
  height: 5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10%;
  position: absolute;
  top: 0;
  left: 0;
}

#main-navigation a {
  text-decoration: none;
  color: white;
  font-weight: bold;
}

#main-navigation a:hover,
#main-navigation a:active {
  color: #cf79f1;
}

#main-navigation h1 a:hover,
#main-navigation h1 a:active {
  color: white;
}

#cut

#welcome {
  background: linear-gradient(to right top, #6305dd, #390281);
  padding: 6rem 12%;
}

#welcome header {
  display: flex;
  align-items: flex-start;
  margin: 3rem auto;
}

#welcome img {
  width: 10rem;
  height: 10rem;
  object-fit: cover;
  object-position: top;
  border: 5px solid white;
  border-radius: 12px;
  background-color: #ffe1bf;
  transform: rotateZ(-5deg);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
}

#welcome h2 {
  font-size: 3.5rem;
  margin: 0 0 0 2rem;
  color: #e4e4e4;
  width: 10rem;
}

#welcome p {
  color: white;
  font-size: 1.5rem;
}

#latest-posts {
  background-color: white;
  padding: 2rem;
  border-radius: 12px;
  width: 60rem;
  margin: -6rem auto 2rem auto;
  box-shadow: 1px 1px 12px rgba(0, 0, 0, 0.4);
}

#latest-posts h2 {
  text-align: center;
}

#latest-posts ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  gap: 1rem;
}

#latest-posts li {
  flex: 1;
}

#about {
  text-align: center;
  padding: 3rem;
  background-color: #e48900;
  margin-top: 5rem;
}

#about h2 {
  font-size: 3rem;
}

#about p {
  font-size: 1.5rem;
  color: #353535;
}