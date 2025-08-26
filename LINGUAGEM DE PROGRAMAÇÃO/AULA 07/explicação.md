<p>Nesta atividade a proposta era de que o usuário fizesse o login e caso fosse validado após alguns segunsdos iria aparecer a mensagem "Redirecionando..." e a página seria redirecionada para algum link. Para isso foi utilizado a função <strong>"setTimeout()"</strong> para que fosse redirecionado para minha página no GitHub.
<br>
<p>Parte que ultilizo a função:</p>
```

 // Aguarda 1.5seg e redireciona o usuário para outra página após validação.
            setTimeout(() => {
                mensagem.innerHTML = "Redirecionando...";
                window.location.href = "https://github.com/dvinacioo";
            },1500);

```

