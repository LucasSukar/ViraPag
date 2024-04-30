//describe = historia; colocar nome da historia
//it = cenario; colocar numero da historia e do cenario; exemplo (h1c1 -> historia 1 cenario 1)

describe('test suite Login', () => {
    it('Login sem cadastro', () => {
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('.text-primary').click()
        cy.get('#username').type('Joaquim')
        cy.get('#email').type('Joaquim@gmail.com')
        cy.get('#password').type('teste')
        cy.get('.btn').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('teste')
        cy.get('.btn').click()
    })
    it('Login com cadastro', () => {
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('teste')
        cy.get('.btn').click()
    })
    it('Cadastro com login', () => {
        cy.visit('/');
        cy.get('.nav-link').click()
        cy.get('.btn-secondary').click()
        cy.get('#username').type('Joaquin')
        cy.get('#email').type('Joaquin@gmail.com')
        cy.get('#password').type('testi')
        cy.get('.btn').click()
        cy.get('.btn-primary').click()
        cy.get('#id_username').type('Joaquin')
        cy.get('#id_password').type('testi')
        cy.get('.btn').click()
    })
    it('Logout', () => {
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('teste')
        cy.get('.btn').click()
        cy.get('.logout > a > .bx').click()
    })
  })