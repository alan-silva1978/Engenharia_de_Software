(function(){const t=document.createElement("link").relList;if(t&&t.supports&&t.supports("modulepreload"))return;for(const o of document.querySelectorAll('link[rel="modulepreload"]'))e(o);new MutationObserver(o=>{for(const r of o)if(r.type==="childList")for(const n of r.addedNodes)n.tagName==="LINK"&&n.rel==="modulepreload"&&e(n)}).observe(document,{childList:!0,subtree:!0});function i(o){const r={};return o.integrity&&(r.integrity=o.integrity),o.referrerPolicy&&(r.referrerPolicy=o.referrerPolicy),o.crossOrigin==="use-credentials"?r.credentials="include":o.crossOrigin==="anonymous"?r.credentials="omit":r.credentials="same-origin",r}function e(o){if(o.ep)return;o.ep=!0;const r=i(o);fetch(o.href,r)}})();function d(a){const t=a.replace(/\D/g,"");if(t.length!==11||/^(\d)\1{10}$/.test(t))return!1;let i=0,e;for(let o=1;o<=9;o++)i+=parseInt(t.substring(o-1,o))*(11-o);if(e=i*10%11,(e===10||e===11)&&(e=0),e!==parseInt(t.substring(9,10)))return!1;i=0;for(let o=1;o<=10;o++)i+=parseInt(t.substring(o-1,o))*(12-o);return e=i*10%11,(e===10||e===11)&&(e=0),e===parseInt(t.substring(10,11))}function l(){const a=document.getElementById("lista-ocorrencias-ativas");if(!a)return;const i=JSON.parse(localStorage.getItem("dadosTurno")||'{"ocorrencias":[]}').ocorrencias||[];if(i.length===0){a.innerHTML='<div style="padding: 10px; background-color: #eafaf1; border-left: 5px solid #27ae60; color: #27ae60;"><strong>Turno em conformidade.</strong> Nenhuma ocorrência ativa registrada.</div>';return}let e='<ul style="list-style: none; padding: 0; margin: 0;">';i.forEach((o,r)=>{e+=`
            <li style="background: #fdedec; padding: 10px; margin-bottom: 8px; border-radius: 4px; border-left: 5px solid #e74c3c; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <span style="flex: 1;"><strong>Ocorrência Ativa:</strong> ${o}</span>
                <button type="button" class="btn-excluir-ocorrencia" data-index="${r}" style="background: #c0392b; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-weight: bold; font-size: 0.85em;">Dar Baixa (Justificar)</button>
            </li>
        `}),e+="</ul>",a.innerHTML=e}function c(){const a=document.getElementById("lista-voluntarios-cadastrados");if(!a)return;const t=JSON.parse(localStorage.getItem("listaVoluntarios")||"[]");if(t.length===0){a.innerHTML="";return}const i=t.map(e=>`
        <div class="card-voluntario">
            <strong>${e.nomeCompleto}</strong>
            <span>${e.areaAtuacao}</span>
            <span class="badge badge-ativo">${e.status}</span>
        </div>
    `).join("");a.innerHTML=`
        <h3>Voluntários Cadastrados Recentemente</h3>
        <div class="lista-cards-voluntarios">${i}</div>
    `}function p(){document.addEventListener("click",function(a){if(a.target.id==="btn-gravar-ocorrencia"){const t=a.target;if(t.disabled)return;t.disabled=!0,t.style.opacity="0.7";const i=document.getElementById("descricao-ocorrencia");if(i.value.trim()===""){Swal.fire("Negado","Descreva a ocorrência antes de registrar.","warning").then(()=>{t.disabled=!1,t.style.opacity="1"});return}const e=JSON.parse(localStorage.getItem("dadosTurno")||'{"ocorrencias":[]}');e.ocorrencias||(e.ocorrencias=[]),e.ocorrencias.push(i.value.trim()),localStorage.setItem("dadosTurno",JSON.stringify(e)),i.value="",l(),Swal.fire("Registrado","Nova ocorrência incorporada ao diário de distribuição.","success").then(()=>{t.disabled=!1,t.style.opacity="1"})}if(a.target.classList.contains("btn-excluir-ocorrencia")){const t=a.target.getAttribute("data-index");Swal.fire({title:"Baixa de Ocorrência",text:"Para manter a Trilha de Auditoria, justifique a exclusão deste registro.",input:"text",inputPlaceholder:"Ex: Item retirado do estoque, ou Erro de registro...",showCancelButton:!0,confirmButtonColor:"#27ae60",cancelButtonColor:"#7f8c8d",confirmButtonText:"Confirmar Baixa",cancelButtonText:"Cancelar",inputValidator:i=>{if(!i)return"A justificativa é obrigatória!"}}).then(i=>{if(i.isConfirmed){const e=JSON.parse(localStorage.getItem("dadosTurno")||'{"ocorrencias":[]}');console.log(`[AUDITORIA] Ocorrência removida: "${e.ocorrencias[t]}". Justificativa: "${i.value}"`),e.ocorrencias.splice(t,1),localStorage.setItem("dadosTurno",JSON.stringify(e)),l(),Swal.fire("Baixa Confirmada","O registro foi arquivado com a justificativa fornecida.","success")}})}}),document.addEventListener("submit",function(a){const t=a.target.querySelector('#cpf, #cpf-login, input[name="cpf"]');if(t)if(d(t.value))t.classList.remove("input-erro");else{a.preventDefault(),t.classList.add("input-erro"),Swal.fire("Atenção","O CPF não é matematicamente válido.","error");return}if(a.target.id==="form-cadastro"){a.preventDefault();const i={id:Date.now(),nomeCompleto:document.getElementById("nome").value,cpf:t.value,telefone:document.getElementById("telefone").value,areaAtuacao:document.getElementById("area").value,status:"Pendente"},e=JSON.parse(localStorage.getItem("listaVoluntarios")||"[]");e.push(i),localStorage.setItem("listaVoluntarios",JSON.stringify(e)),a.target.reset(),c(),Swal.fire("Recebido!","Cadastro realizado.","success")}if(a.target.id==="form-login"){if(a.preventDefault(),document.getElementById("senha").value.length<6){Swal.fire("Acesso Negado","A senha requer mínimo de 6 caracteres.","error");return}window.location.hash="#diario"}if(a.target.id==="form-diario"){a.preventDefault();const i=a.target.querySelector('button[type="submit"]');if(i&&i.disabled)return;i&&(i.disabled=!0,i.style.opacity="0.7");const e=document.getElementById("itensDistribuidos"),o=document.getElementById("assuncao");let r=!0;if(e.value.trim()===""||e.value<=0?(e.classList.add("input-erro"),r=!1):e.classList.remove("input-erro"),o.value.trim()===""?(o.classList.add("input-erro"),r=!1):o.classList.remove("input-erro"),!r){Swal.fire("Atenção","Preencha a quantidade distribuída e a data.","warning").then(()=>{i&&(i.disabled=!1,i.style.opacity="1")});return}const n=JSON.parse(localStorage.getItem("dadosTurno")||'{"ocorrencias":[]}');n.itensDistribuidos=e.value,n.assuncao=o.value,localStorage.setItem("dadosTurno",JSON.stringify(n)),a.target.reset(),Swal.fire("Sucesso!","Turno registrado com sucesso.","success").then(()=>{i&&(i.disabled=!1,i.style.opacity="1"),window.dispatchEvent(new Event("hashchange"))})}})}function f(){if(document.getElementById("form-diario")){const t=JSON.parse(localStorage.getItem("dadosTurno")||"{}"),i=document.getElementById("ultimo-registro");i&&t.itensDistribuidos&&(i.innerHTML=`<span style="display: block; color: #e67e22; font-weight: bold; margin-bottom: 10px;">Último registro de distribuição: ${t.itensDistribuidos} kits</span>`),l()}document.getElementById("lista-voluntarios-cadastrados")&&c()}function m(){document.querySelectorAll('#cpf, #cpf-login, input[name="cpf"]').forEach(e=>{const o=document.getElementById(e.id+"-erro");e.addEventListener("input",function(r){let n=r.target.value.replace(/\D/g,"");n.length>11&&(n=n.slice(0,11)),n=n.replace(/(\d{3})(\d)/,"$1.$2"),n=n.replace(/(\d{3})(\d)/,"$1.$2"),n=n.replace(/(\d{3})(\d{1,2})$/,"$1-$2"),r.target.value=n,n.length===14?d(n)?(e.classList.remove("input-erro"),e.classList.add("input-sucesso"),e.setAttribute("aria-invalid","false"),o&&(o.textContent="",o.style.display="none")):(e.classList.remove("input-sucesso"),e.classList.add("input-erro"),e.setAttribute("aria-invalid","true"),o&&(o.textContent="CPF inválido. Verifique os números digitados.",o.style.display="block")):(e.classList.remove("input-erro","input-sucesso"),e.removeAttribute("aria-invalid"),o&&(o.textContent="",o.style.display="none"))})});const t=document.getElementById("telefone");if(t){const e=document.getElementById("telefone-erro");t.addEventListener("input",function(o){let r=o.target.value.replace(/\D/g,"");r.length>11&&(r=r.slice(0,11)),r=r.replace(/^(\d{2})(\d)/g,"($1) $2"),r=r.replace(/(\d)(\d{4})$/,"$1-$2"),o.target.value=r;const n=r.replace(/\D/g,"");n.length===11?(t.classList.remove("input-erro"),t.classList.add("input-sucesso"),t.setAttribute("aria-invalid","false"),e&&(e.textContent="",e.style.display="none")):n.length>0?(t.classList.remove("input-sucesso"),t.classList.add("input-erro"),t.setAttribute("aria-invalid","true"),e&&(e.textContent="Telefone incompleto. Use o formato (00) 00000-0000.",e.style.display="block")):(t.classList.remove("input-erro","input-sucesso"),t.removeAttribute("aria-invalid"),e&&(e.textContent="",e.style.display="none"))})}const i=document.getElementById("itensDistribuidos");i&&i.addEventListener("input",function(e){e.target.value=e.target.value.replace(/\D/g,"")})}const s=document.getElementById("app-root");p();function u(){const a=window.location.hash||"#home";s.innerHTML="",a==="#home"?s.innerHTML=`
            <section id="sobre" style="text-align: center; padding: 20px;">
                <h2 id="titulo-secao">Bem-vindo à ONG Ação e Vida</h2>
                <p style="font-size: 1.1em; margin-bottom: 20px;">Trabalhamos para levar esperança, suprimentos e apoio logístico para comunidades em situação de vulnerabilidade.</p>
                <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                    <a href="#acoes" style="padding: 12px 24px; text-decoration: none; background-color: #3498db; color: white; border-radius: 5px; font-weight: bold;">Conheça Nossas Ações</a>
                    <a href="#voluntarios" style="padding: 12px 24px; text-decoration: none; background-color: #27ae60; color: white; border-radius: 5px; font-weight: bold;">Quero ser Voluntário</a>
                </div>
            </section>
        `:a==="#acoes"?s.innerHTML=`
            <section id="painel-acoes">
                <h2 id="titulo-secao">O Nosso Impacto Social</h2>
                <article style="background-color: #f9f9f9; padding: 15px; margin-bottom: 15px; border-left: 5px solid #27ae60;">
                    <h3>Distribuição de Alimentos (Em Andamento)</h3>
                    <p>Atuamos na linha de frente garantindo a segurança alimentar de 500 famílias cadastradas na região metropolitana.</p>
                </article>
                <div style="text-align: center; margin-top: 20px;">
                    <a href="#voluntarios" style="padding: 10px 20px; background-color: #2c3e50; color: white; text-decoration: none; border-radius: 5px;">Junte-se à Equipe</a>
                </div>
            </section>
        `:a==="#voluntarios"?s.innerHTML=`
            <section id="cadastro-voluntario">
                <h2 id="titulo-secao">Cadastro de Novos Voluntários</h2>
                <form id="form-cadastro">
                    <fieldset>
                        <legend>Dados Pessoais</legend>
                        <label for="nome">Nome Completo:</label>
                        <input type="text" id="nome" placeholder="Digite seu nome completo" required>

                        <label for="cpf" id="label-cpf">CPF (Apenas números):</label>
                        <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" aria-describedby="cpf-erro" required>
                        <span id="cpf-erro" class="mensagem-erro" role="alert"></span>

                        <label for="telefone">Telefone de Contato:</label>
                        <input type="tel" id="telefone" name="telefone" placeholder="(00) 00000-0000" aria-describedby="telefone-erro" required>
                        <span id="telefone-erro" class="mensagem-erro" role="alert"></span>

                        <label for="area">Área de Atuação de Interesse:</label>
                        <select id="area" name="area">
                            <option value="Distribuição de Alimentos">Distribuição de Alimentos</option>
                            <option value="Administrativo">Administrativo</option>
                            <option value="Captação de Recursos">Captação de Recursos</option>
                        </select>
                    </fieldset>
                    <button type="submit" style="background-color: #27ae60;">Enviar Solicitação</button>
                </form>

                <div id="lista-voluntarios-cadastrados" style="margin-top: 25px;"></div>
            </section>
        `:a==="#login"?s.innerHTML=`
            <section id="autenticacao" style="max-width: 400px; margin: 0 auto; text-align: center;">
                <h2 id="titulo-secao">Área Restrita</h2>
                <form id="form-login">
                    <label for="cpf-login" style="text-align: left;">CPF Operacional:</label>
                    <input type="text" id="cpf-login" required style="margin-bottom: 15px;" aria-describedby="cpf-login-erro">
                    <span id="cpf-login-erro" class="mensagem-erro" role="alert"></span>
                    <label for="senha" style="text-align: left;">Senha de Acesso:</label>
                    <input type="password" id="senha" required style="margin-bottom: 20px;">
                    <button type="submit" style="background-color: #e74c3c;">Autenticar e Assumir Turno</button>
                </form>
            </section>
        `:a==="#diario"&&(s.innerHTML=`
            <section id="formulario-registro">
                <h2 id="titulo-secao">Diário de Distribuições</h2>

                <!-- PELOTÃO 1: REGISTRO DO TURNO -->
                <form id="form-diario" style="margin-bottom: 30px; padding-bottom: 20px; border-bottom: 2px solid #ccc;">
                    <fieldset>
                        <legend>1. Registro do Turno de Distribuição</legend>
                        <div id="ultimo-registro"></div>
                        <label for="itensDistribuidos">Quantidade de Kits Distribuídos:</label>
                        <input type="number" id="itensDistribuidos" name="itensDistribuidos">

                        <label for="assuncao">Data e Hora de Início do Turno:</label>
                        <input type="datetime-local" id="assuncao" name="assuncao">

                        <button type="submit" style="background-color: #2c3e50;">Registrar Turno</button>
                    </fieldset>
                </form>

                <!-- PELOTÃO 2: OCORRÊNCIAS NA DISTRIBUIÇÃO -->
                <div id="gestao-ocorrencias">
                    <fieldset>
                        <legend>2. Ocorrências e Itens Impróprios para Doação</legend>

                        <div id="lista-ocorrencias-ativas"></div>

                        <details style="margin-top: 15px; padding: 10px; background-color: #f9f9f9; border-radius: 5px;">
                            <summary style="font-weight: bold; color: #e74c3c; cursor: pointer;">+ Reportar Nova Ocorrência</summary>

                            <label for="descricao-ocorrencia">Descrição da Ocorrência:</label>
                            <input type="text" id="descricao-ocorrencia" placeholder="Ex: Alimento com validade vencida">

                            <button type="button" id="btn-gravar-ocorrencia" style="background-color: #e67e22; margin-top: 10px;">Registrar Ocorrência</button>
                        </details>
                    </fieldset>
                </div>
            </section>
        `),m(),f();const t=s.querySelector("#titulo-secao");t&&(t.setAttribute("tabindex","-1"),t.focus())}window.addEventListener("hashchange",u);window.addEventListener("load",u);
