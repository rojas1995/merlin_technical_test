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

		cy.origin("https://es.wikipedia.org/", () => {
			cy.get("p")
				.contains(
					"convirtiéndose en el primer proceso industrial completamente automatizado"
				)
				.then(() => {
					cy.screenshot({overwrite:true});
				});
		});
	});
});
