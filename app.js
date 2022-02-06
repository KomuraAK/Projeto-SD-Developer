//Autor: Anthony Farias

//Módulos
const express = require("express");
const session = require("express-session");
const bodyParser = require("body-parser");

//USUÁRIO E SENHA DE TESTE
var login = "admin";
var password = "7ç5Afg8yba45hhKlÇ";

//Simplifica o código
const app = express();
var path = require("path");
const port = 3000; //Porta do servidor é a 3000

//Chave de sessão
app.use(session({ secret: "7af2freg3r5r3stghaw" }));

//Conexão dos arquivos
app.use(bodyParser.urlencoded({ extended: true }));
app.engine("html", require("ejs").renderFile);
app.set("view engine", "html");
app.use("/public", express.static(path.join(__dirname, "public")));
app.set("views", path.join(__dirname, "views"));
app.use("/styles", express.static("styles"));
app.use("/img", express.static("img"));

//Rotas de autenticação
app.post("/", (req, res) => {
  if (req.body.login == login && req.body.password == password) {
    req.session.login = login;
    res.redirect("http://127.0.0.1:8050/");
  } else {
    res.render("index");
  }
});

app.get("/", (req, res) => {
  res.render("index");
  if (req.session.login) {
    res.redirect("http://127.0.0.1:8050/");
  } else {
    res.render("index");
  }
});

//Inicia o servidor
app.listen(port, () => {
  console.log("Servidor rodando com sucesso!");
});
