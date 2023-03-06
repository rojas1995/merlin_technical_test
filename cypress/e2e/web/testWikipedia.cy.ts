describe("example to-do app", () => {
	//we don't need a beforeach or aftereach block

	it("check the first year that an automation was made", () => {
		cy.visit("/");
		//I don't use the ids of the html elements because the values of these ids on Google page might change in different executions and browsers
		cy.get("button").contains("Aceptar todo").click();
		cy.get("input").first().focus().type("automatización");
		cy.get("form")
			.submit()
			.then(() => {
				cy.get("a").contains("wikipedia").click();
			});
		//use origin to be able to go to another domain
		cy.origin("https://es.wikipedia.org/", () => {
			cy.get("p")
				.contains(
					"convirtiéndose en el primer proceso industrial completamente automatizado" //I think that this paragraph contains the information about the first automation process
				)
				.then(() => {
					cy.screenshot({overwrite:true}); //take the screenshot and overwrite the picture for each run
				});
		});
	});
	//I have tested this code with Chrome, Edge and Electron, with Chrome when you re-run the test some times don't get the <a> tags of the search result, instead get the <a> tags of the firts view of Google
	//With Edge the command origin work but throws an uncaught exception, I try to mitigate it with the code on file e2e.ts (https://docs.cypress.io/api/events/catalog-of-events#Examples), 
	//with Chrome and Electron it works but not with Edge, I need more time to investigate this
	//I can't run the test on Safari, I have windows and I haven't any tool to run the test on ios
});
