 function validaForm (frm){
		if (frm.nome.value==""||frm.nome.value==null){
			alert("Preencha o campo do Nome!!!");
			frm.nome.focus();
			return false;}
		if (frm.data.value==""||frm.data.value==null){
		   alert("Preencha o campo da data de nascimento!!!");
		   frm.data.focus();
		   return false;}
		if (frm.rg.value==""||frm.rg.value==null){
		   alert("Preencha o campo do RG!!!");
		   frm.rg.focus();
		   return false;}
		if (frm.estado.value==""||frm.estado.value==null){
		   alert("Preencha o campo do estado!!!");
		   frm.estado.focus();
		   return false;}
		if (frm.cidade.value==""||frm.cidade.value==null){
		   alert("Preencha o campo da cidade!!!");
		   frm.cidade.focus();
		   return false;}
		if (frm.bairro.value==""||frm.bairro.value==null){
		   alert("Preencha o campo do bairro!!!");
		   frm.bairro.focus();
		   return false;}
		
		if (frm.rua.value==""||frm.rua.value==null){
		   alert("Preencha o campo da rua!!!");
		   frm.rua.focus();
		   return false;}
		if (frm.num.value==""||frm.num.value==null){
		   alert("Preencha o campo do número!!!");
		   frm.num.focus();
		   return false;}
		if (frm.quali.value==""||frm.quali.value==null){
		   alert("Preencha o campo das qualificações!!!");
		   frm.quali.focus();
		   return false;}
		if (frm.email.value==""||frm.email.value==null){
		   alert("Preencha o campo do email!!!");
		   frm.email.focus();
		   return false;}
		if (frm.senha.value==""||frm.senha.value==null){
		   alert("Preencha o campo da senha!!!");
		   frm.senha.focus();
		   return false;}
		if (frm.servico.value==""||frm.servico.value==null){
		   alert("Preencha o campo do tipo de serviço prestado!!!");
		   frm.servico.focus();
		   return false;}
		
		}