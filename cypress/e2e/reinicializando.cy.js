describe('test suite reinicializando os testes', () => {
    it('Adicionar livro', () => {
        cy.visit('/admin/');
        cy.get('#id_username').type('admin')
        cy.get('#id_password').type('1234')
        cy.get('.submit-row > input').click()
        cy.get('.model-user > th > a').click()
        cy.get(':nth-child(1) > .action-checkbox > .action-select').click()
        cy.get(':nth-child(2) > .action-checkbox > .action-select').click()
        cy.get('select').select('Delete selected users')
        cy.get('.button').click()
        cy.get('div > [type="submit"]').click()
    })
})