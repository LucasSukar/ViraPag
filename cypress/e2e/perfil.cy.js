//describe = historia; colocar nome da historia
//it = cenario; colocar numero da historia e do cenario; exemplo (h1c1 -> historia 1 cenario 1)

describe('test suite alteracao de senha', () => {
    it('Login + Mudar Senha', () => {
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('teste')
        cy.get('.btn').click()
        cy.get(':nth-child(2) > a > .bx').click()
        cy.get('.btn').click()
        cy.get('#senha_antiga').type('teste')
        cy.get('#nova_senha').type('testando')
        cy.get('#confirmar').type('testando')
        cy.get('.btn').click()
    })
})