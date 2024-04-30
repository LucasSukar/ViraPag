//describe = historia; colocar nome da historia
//it = cenario; colocar numero da historia e do cenario; exemplo (h1c1 -> historia 1 cenario 1)

describe('test suite biblioteca', () => {
    it('Adicionar livro', () => {
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('testando')
        cy.get('.btn').click()
        cy.get(':nth-child(3) > a > .bx').click()
        cy.get('.btn').click()
        cy.get('#titulo').type('Guardiola Confidencial')
        cy.get('#autor').type('Marti Perarnau')
        cy.get('#anopublicado').type('2010')
        cy.get('.btn').click()
        //cy.get('.card-title').invoke('text').should('Guardiola Confidencial')
    })
    it('Entrar no livro', () => {
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('testando')
        cy.get('.btn').click()
        cy.get(':nth-child(3) > a > .bx').click()
        cy.get('.list-group-item').click()
        cy.get('.col-md-8 > [href="/mainapp/biblioteca/"]').click()
    })
    it('Editar livro', () => {
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('testando')
        cy.get('.btn').click()
        cy.get(':nth-child(3) > a > .bx').click()
        cy.get('.list-group-item').click()
        cy.get('[href="/mainapp/atualizar/18/"]').clear()
        cy.get('[href="/mainapp/atualizar/18/"]').click()
        cy.get('#anopublicado').type('2014')
        cy.get('.btn').click()
    })
    it('Excluir livro', () => {
        cy.visit('/');
        cy.get('.nav-link > .logosomb').click()
        cy.get('.btn-primary').click()
        cy.get('#id_username').type('Joaquim')
        cy.get('#id_password').type('testando')
        cy.get('.btn').click()
        cy.get(':nth-child(3) > a > .bx').click()
        cy.get('.list-group-item').click()
        cy.get('.col-md-8 > .btn-danger').click()
        cy.get('form > .btn').click()
    })
  })