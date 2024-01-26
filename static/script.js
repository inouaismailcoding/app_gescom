$(document).ready(function () {
  let data;
  let data_serialise=[];
  let val_form=[];
  let data_to_print_to_table=[];
  
  //let amount=document.getElementById('id_amount');

  // On verifie si le select mouvement existe dans le HTML
  if(document.getElementById('select_mouvement')){
      $(document).on('change','#select_mouvement',(e)=>{
        e.preventDefault();
        let mouvement=$("#select_mouvement").val();
        $("#id_mouvement").val(mouvement);
      });
  }
  // On verifie si le select Intervenant existe dans le HTML
  if(document.getElementById('select_intervenant')){
      $(document).on('change','#select_intervenant',(e)=>{
        e.preventDefault();
        let intervenant=$("#select_intervenant").val();
        $("#id_intervenant").val(intervenant);
      });
  }

  $(document).on('click','#modal-choice',(e)=>{
    e.preventDefault();    
    $.ajax({
      url:'',
      method:'get',
      data:"fetchAll=fetchAll",
      success:(res)=>{
        data=res;
      }
    });
  });

  // Procedure lors du changement de category dans le select Article
  $(document).on('change','#id_category',(e)=>{
    e.preventDefault();
    let selectCategory=document.getElementById("id_category");
    let selectArticle=document.getElementById("id_article");
    
    // On filtre les donnée
    articles=data.article
    listArticle=articles.filter((row)=>{
      return row.category_id == selectCategory.value 
    });
    // On suprime tout les options du select 
    deleteOption(selectArticle);
    // On ajoute les options avec les nouvelle données
    addOptionSelectArticle(selectArticle, listArticle);

  });

  // Procedure lors du changement d'article dans le select Emballage
  $(document).on('change','#id_article',(e)=>{
    e.preventDefault();
    let selectArticle=document.getElementById("id_article");
    let selectPackage=document.getElementById("id_package");
    
    // On filtre les donnée
    articles=data.article
    article=articles.filter((row)=>{
      return row.id == selectArticle.value 
    });
    // On recupere le montant du prix unitaire
    if(document.getElementById('id_price_unit')){
      document.getElementById('id_price_unit').value = article[0].price
    }
    packages=data.package
    listPackage=packages.filter((row)=>{
      return row.id == article[0].package_id 
    });
    // On suprime tout les options du select 
    deleteOption(selectPackage);
    // On ajoute les options avec les nouvelle données
    addOptionSelectEmballage(selectPackage, listPackage)

  });

  // Pour ajouter dynamiquement le montant total
    // en fonction de la quantité et du price
    
    $(document).on("input", "#id_price", (e) => {
      e.preventDefault();
      calculateAmountRow();
    });
    $(document).on("input", "#id_quantity", (e) => {
      e.preventDefault();
      calculateAmountRow();
    });

    // Procedure pour recuperer le formulaire rempli et ajouter a la ligne du tableau
    $(document).on('click','#btn-form-items',(e)=>{
      e.preventDefault();
      let form=$('#form-items');
      let category=document.getElementById('id_category');
      let article=document.getElementById('id_article');
      let package=document.getElementById('id_package');
      let row=stringToArray(form.serialize());
      data_serialise.push(form.serialize());
      val_form.push(row);
      row['category']=category.options[category.selectedIndex].text;
      row['article']=article.options[article.selectedIndex].text;
      row['package']=package.options[package.selectedIndex].text;
      data_to_print_to_table.push(row);
      form[0].reset();
      addItemTbody(data_to_print_to_table);
      addDataToForm(data_serialise);
      sumAmount(val_form);
      sumQuantity(val_form);
      
      
    });
    // Procedure lors d'un click pour supprimer une ligne de donnée
    $(document).on('click','.btn-delete-row',(e)=>{
      e.preventDefault();
      let index=e.currentTarget.dataset.index-1;
      deleteRowArray(index,val_form);
      deleteRowArray(index,data_to_print_to_table);
      deleteRowArray(index,data_serialise);
      addItemTbody(data_to_print_to_table);
      addDataToForm(data_serialise);
      sumAmount(val_form);
      sumQuantity(val_form);
    });

    // Procedure lorsqu'on veut supprimer une ligne de donnée
    $(document).on('click','.btn-edit-row',(e)=>{
      e.preventDefault();
      let index =e.currentTarget.dataset.index-1;
      console.log("Table Html : ",data_to_print_to_table[index]);
      console.log("data server : ",val_form[index]);
    });
    
    // Procedure qui permet de recuperer le type de fichier a télécharger
      document.getElementById('select-type-download-file').onchange=(e)=>{
       e.preventDefault();
       type_file=$("#select-type-download-file");
       val_file=type_file.val();
       let download_type=$('#download-type')
       
        if($('#download').css('display')=== 'none')
       {
           r="  ";
           download_type.text(r+val_file);
           $("#download").show('1s');    
       }else{download_type.text("  "+val_file);}
       
      
      }  
       // On reinitialise le formulaire de selection du type de fichier et oçn masque le boutton
     document.getElementById("download").onclick=(e)=>{
      e.preventDefault();
      
      let form =$('#form-select-type-file-download');
      let format =document.getElementById('select-type-download-file').value;
       exportToTbleHtmlToFormat(format);
      form[0].reset();
      $('#download').hide('1s');
  }
// function pour telecharger html sous different forme
function exportToTbleHtmlToFormat(format) {
 
 if (format==='excel'){
   let ws = XLSX.utils.table_to_sheet(table);
   var wb = XLSX.utils.book_new();
   XLSX.utils.book_append_sheet(wb, ws, "Feuille1");
   XLSX.writeFile(wb, 'export.xlsx');}
 
 if(format ==='json'){
   let ws = XLSX.utils.table_to_sheet(table);
   var json = XLSX.utils.sheet_to_json(ws, { header: 1 });
   var blob = new Blob([JSON.stringify(json)], { type: "application/json" });
   saveAs(blob, "export.json");
 }
 if (format ==='csv'){
   let ws = XLSX.utils.table_to_sheet(table);
   var csv = XLSX.utils.sheet_to_csv(ws);
   var blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
   saveAs(blob, "export.csv");}

 }

  function saveAs(blob, fileName) {
      var link = document.createElement("a");
      link.href = window.URL.createObjectURL(blob);
      link.download = fileName;
      link.click();
  }

    // Function pour ajouter les elements de la table
    function addItemTbody(data){
      let content="";
      let tbody=document.getElementById('tbody');
      tbody.innerHTML="";
      let r=1;
      data.forEach(element => {
        content+="<tr>";
        content+="<td>"+r+"</td>";
        for(let i in element){
          
          content+="<td>"+element[i]+"</td>";
          
              }
          content+="<td><button class='btn btn-edit-row' data-index='"+r+"'><span class='fa fa-edit'></span>Edit</button>";
          content+="<button  class='btn btn-delete-row' data-index='"+r+"'><span class='fa fa-trash'></span>Delete</button></tr>";
          r+=1;
      });
      tbody.innerHTML=content;
    }
    // Function Pour supprimer une ligne dans le tableau html et le tableau de donnée
    function deleteRowArray(index,data){
      data.splice(index,1);
    }
    // Function pour convertir les chaine de caractere en tableau
    function stringToArray(form_items_data){
      listElement=form_items_data.split("&");
      let tab={}
      listElement.forEach(element => {
        f=element.split('=');
        tab[f[0]]=f[1];
        });
      return tab;

    }
    // function Pour recuperer les enregistrements du formulaire
    function addDataToForm(data){
      let line_data=document.getElementById('form-data-lines');
      line_data.innerHTML="";
      var lineHtml="";
      data.forEach(element => {
        
            lineHtml +="<div class='line'>";
            lineHtml +="<input type='hidden' name='lines[]' value='"+element+"'>";
            lineHtml +="</div>";
      });
      line_data.innerHTML=lineHtml;
    }
    // Function pour calculer automatiquement le total
    function calculateAmountRow(){
      if(document.getElementById('id_price_unit')){
        quantity=document.getElementById('id_quantity');
        total=document.getElementById('id_total');
        price_unit=document.getElementById('id_price_unit');
        if ( quantity.value =='' | price_unit.value == ''){
          total.value=''
        }else{
          total.value = parseInt(price_unit.value) * parseInt(quantity.value);
        }
      }
      else if(document.getElementById('id_price')){
        quantity=document.getElementById('id_quantity');
        total=document.getElementById('id_total');
        price_unit=document.getElementById('id_price');
        if ( quantity.value =='' | price_unit.value == ''){
          total.value=''
        }else{
          total.value = parseInt(price_unit.value) * parseInt(quantity.value);
        }
      }
    }
    
    // Function pour recuperer les données du formualire
    // comparé les données avec ceux du tableau data 
    // Et l'afficher sur le tableau

    function recoveryDataToForm(val_form){
      listArticle=data.article;
      listCategory=data.category;
      listPackage=data.package;
      val=val_form;
      row={};
      val.forEach(element=>{
        row={};
        cat=listCategory.filter((e)=>{
           return  e.id == element['category'];
        });
        art=listArticle.filter((e)=>{
         return  e.id == element['article'];
      });
      pack=listPackage.filter((e)=>{
        return  e.id == element['package'];
     });
     element['category']=cat[0].category;
     element['article']=art[0].article;
     element['package']=pack[0].package;

      });

      console.log(val);
    }

  // function qui supprime toutes les options d'un select
  function deleteOption(select) {
    while (select.firstChild) {
      select.removeChild(select.firstChild);
    }
  }

  // Function créer les options dans les selects articles
  function addOptionSelectArticle(select, listArticles) {
    opt = document.createElement("option");
    opt.value = "";
    opt.text = "-----------";
    select.add(opt);
    listArticles.forEach((e) => {
      option = document.createElement("option");
      option.value = e.id;
      option.text = e.article;
      select.add(option);
    });
  }

  // Function créer les options dans les selects Emballages
  function addOptionSelectEmballage(select, listEmballage) {
    opt = document.createElement("option");
    opt.value = "";
    opt.text = "------";
    select.add(opt);
    listEmballage.forEach((e) => {
      option = document.createElement("option");
      option.value = e.id;
      option.text = e.package;
      select.add(option);
    });
  }

  // On cree une fonction pour recuperer la somme d(un tableau)
  function sumAmount(data) { 
    let sum=0;
    if(document.getElementById('id_amount')){
      data.forEach(e=>{
        sum=sum+parseInt(e.amount)
    });  $("#id_amount").val(sum);
  }
}

  // On cree une fonction pour recuperer la somme des quantités
  function sumQuantity(data) { 
    let sum=0;
    if(document.getElementById('id_full_quantity')){
      data.forEach(e=>{
        sum=sum+parseInt(e.quantity)
    });
    $("#id_full_quantity").val(sum);
    }
  }
});