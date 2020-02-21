Main = {
	getExtrasHTML({type,numSelected}){
		return `<div class="extras" id="${type}-${numSelected}">
		<i class="fa fa-chevron-left"></i>
		<span>Item no.${numSelected}</span>
		<i class="fa fa-chevron-right"></i>
		<div class="sidedishes">
		  <input type="checkbox" value="Majoneza">
		  <span class="checkboxtext">Majoneza</span>
		</div>
		<div class="sidedishes">
		  <input type="checkbox" value="Salata">
		  <span class="checkboxtext">Salata</span>
		</div>
		<div class="sidedishes">
		  <input type="checkbox" value="Rajcica">
		  <span class="checkboxtext">Rajcica</span>
		</div>
  	 	 </div>`
	},
	start() {
		$("input[type='checkbox']").change(function () {
			const item = $(this).siblings('input[type="number"]')[0];
			let checkboxElem = $(this).parents('.articles');
			let selected = $(this).is(":checked");

			if (selected) {
				item.value++;
			}
			else {
				item.value = 0;
			}
			Main.changePrice();
			Main.dynamicExtrasPositioning({checkboxElem, selected,numSelected:1});
		})
		
		$("input[type='number']").change(function () {
			let checkboxElem = $(this).parents('.articles');
			Main.changePrice();
			let numSelected = parseInt($(this).val());			
			Main.dynamicExtrasPositioning({checkboxElem, selected:null, numSelected});
		})

		$(document).on('click',".fa-chevron-left" , function() {
			
			let parent = $(this).parents('.extras');
			
			Main.changeActive({elem:parent,isLeft:true});
		})
		$(document).on('click',".fa-chevron-right" , function() {
			
			let parent = $(this).parents('.extras');
			
			Main.changeActive({elem:parent,isLeft:false});
		})

		$(".register-button").on('click', function(){
			Main.registerUser();
		})

		$(".login-button").on('click', function(){
			Main.loginUser();
		})

		$(".orderConfirm-button").on('click', function(){
			Main.confirmOrder();
		})

		$(".review-button").on('click', function(){
			Main.saveReview();
		})

		$(".addFood-button").on('click', function(){
			Main.addFood();
		})
	},

	changePrice() {
		const allInputs = $("input[type='number']");
		let prices = 0;
		allInputs.each(function () {
			const itemCount = $(this).val();
			const checkbox = $(this).siblings("input[type='checkbox']");
			if (itemCount > 0) {
				checkbox.prop('checked', true)
				const price = $(this).siblings(".price").data("price")
				prices += price * itemCount
			} else {
				checkbox.prop('checked', false)
			}

		})
		$("#price").text(prices);
	},

	changeActive({elem, isLeft}){
		let currentId = elem.attr("id")
		currentId =currentId.split("-")
		let type = currentId[0]
		let subId = parseInt(currentId[1])
		if(isLeft)
		{
			$(`#${type}-${subId-1}`).css("display","inline-block")
		}
		else{
			$(`#${type}-${subId+1}`).css("display","inline-block")
		}
		elem.css("display","none")

		
		
	},
	dynamicExtrasPositioning({checkboxElem, selected, numSelected}) {

		

		// Vidi jel element koji ima otvoreno extras
		// Ako je taj elem onda gledaj jel broj 0, ako je onda makni extras
		// Ako nije 0 nego veci od 0 gledaj ima li otvoren extras ako ima ostavi ga otvorenim ili dodaj jos jedan extras za broj dva
		let elemMinus;
		let hasCurrent = false;

		let type = checkboxElem.data('name');
		
		if(selected==false){
			$("[id^="+type+"]").remove();
			return
		}

		// This is for decreasing
		try {
			let current= checkboxElem.siblings(`#${type}-${numSelected}`);	
			
			hasCurrent = current.length==0 ? false : true;					 
		} catch (error) {			
		}
		// This is for increasing
		try {
			elemMinus  = checkboxElem.siblings(`#${type}-${numSelected-1}`);						 
			 
		} catch (error) {			
		}
		try {
			$(`#${type}-${numSelected+1}`).remove();
			$(`#${type}-${numSelected}`).css("display","inline-block");
		} catch (error) {
			// Fail silently
			
		}
		
		if(numSelected>1){			
			if(!hasCurrent){
				elemMinus.css("display","none")
				let exHTML = Main.getExtrasHTML({type, numSelected});
				
				$(exHTML).insertAfter(checkboxElem[0]);
			}
			
		}else if (numSelected == 1){
			if(!hasCurrent){
				let exHTML = Main.getExtrasHTML({type, numSelected});
				
				$(exHTML).insertAfter(checkboxElem[0]);
			}
		}
		else{
			$(".extras").remove();
		}
		
	},
	registerUser(){

		let name= $("input[name='username']").val();
		let adresa= $("input[name='adresa']").val();
		let password= $("input[name='password']").val();		
		
		fetch('/register', {
	method: 'POST',
	headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json'
	  },
    body: JSON.stringify({
		username:name,
		adresa:adresa,
		password:password
	})
  }).then(function(response) {
    return response.json();
  }).then(function(data) {
	  
   if(!data.success)
   {
	   alert(data.message)
   }
   else{
	   window.location.href = "login";
   }
  })
	},

	loginUser(){

		let name= $("input[name='username']").val();
		let password= $("input[name='password']").val();	
			
		fetch('/login', {
	method: 'POST',
	headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json'
	  },
    body: JSON.stringify({
		username:name,
		password:password
	})
  }).then(function(response) {
    return response.json();
  }).then(function(data) {
	  
   if(!data.success)
   {
	   alert(data.message)
   }
   else{
   	   document.cookie = "username="+name;
	   
	   if(data.vlasnik)
	   {
		window.location.href = "restaurantedit/" + name;
	   }
	   else
	   {
		window.location.href = "order";
	   }
	
   }
  });
	},

	confirmOrder() {
		const allInputs = $("input[type='number']");
		let prices = 0;
		let itemCount = 0;
		allInputs.each(function () {
			const checkbox = $(this).siblings("input[type='checkbox']").is(":checked");
			if (checkbox)
			{
				itemCount++;
			}
			// window.location.reload();
		})

		if (itemCount > 0) {
			alert("Vaša narudžba je zaprimljena.")
			
		} else {
			alert("Niste odabrali artikle.");
		}

		$("#price").text(prices);
	},

	saveReview()
	{				
		let reviewDesc = $("textarea[name='reviewDesc']").val();
		//let rating= document.querySelector('input[name="rating"]:checked').value;		
		
		let rating = document.querySelector('input[name="rating"]:checked');
		let value;
		try {
			value = rating.value
		} catch (error) {
			value = null
		}
		
		let username = document.cookie;
		if(username.includes(";")){
			username = username.split(";")[1]
		}
		username = username.split("=")[1]
		
		let pathArray = window.location.pathname.split('/');
		let restaurantName = pathArray[pathArray.length-1]
		
		fetch('/reviews', {
	method: 'POST',
	headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json'
	  },
    body: JSON.stringify({
		reviewDesc:reviewDesc,
		rating:value,
		username:username,
		restaurant_name:restaurantName
	})
  }).then(function(response) {
    return response.json();
  }).then(function(data) {
	  
	alert(data.message)
	if(data.success)
   {
		window.location.reload();
   }
	
  });
	},

	addFood()
	{				
		let foodName = $("input[name='foodName']").val();
		let foodPrice = $("input[type='number']").val();
				
		let pathArray = window.location.pathname.split('/');
		let restaurantName = pathArray[pathArray.length-1]
		
		fetch('/addfood', {
	method: 'POST',
	headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json'
	  },
    body: JSON.stringify({
		foodName:foodName,
		foodPrice:foodPrice,
		restaurant_name:restaurantName
	})
  }).then(function(response) {
    return response.json();
  }).then(function(data) {
	  
	alert(data.message)
	if(data.success)
   {
		window.location.reload();
   }
	
  });
	}
}	

$(document).ready(Main.start)