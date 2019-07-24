from odoo import models, fields, api 
class TablePays(models.Model):
    _name='gestion.pays'
    _description = 'fifa pays'
    nompays = fields.Char('Nom Pays', size=8, required=True) 
    superficie = fields.Char('Superficie Pays', size=32, required=True) 
    continent = fields.Char('Continent Pays', size=32, required=True)
class TableEditionCoupeDuMonde(models.Model):
    _name='gestion.edition'
    _description = 'Edition du coupe de monde'
    annee = fields.Date('Annee', required=True) 
    paysOrganisateur = fields.Many2one('gestion.pays', 'Nom Pays')  
    paysVainqueur = fields.Many2one('gestion.pays', 'Nom Pays')  
class ParticipationPays(models.Model):
    _name='gestion.participation'
    _description='gestionner de la participation'
    nompays = fields.Char('Nom Pays', size=8, required=True)
    annee_id = fields.Many2one('gestion.edition', 'Annee')
    entraineur = fields.Char('Entraineur', size=20 , required=True)
    parcours = fields.Char('Parcours', size=20 ,required=True)
class TableMatch(models.Model):
    _name = 'gestion.match'
    _description = 'gestion match'
    nomPays1 = fields.Many2one('gestion.pays', 'Nom Pays')
    nomPays2 = fields.Many2one('gestion.pays', 'Nom pays')
    anneem = fields.Many2one('gestion.edition', 'Annee')
    nbreButsMarque1=fields.Integer('Nombre Buts Marque 1 ', required=True)
    nbreButsMarque2=fields.Integer('Nombre Buts Marque 2 ', required=True)
    phase = fields.Char('Phase', required=True)
class Joueur(models.Model):
    _name = 'gestion.joueur'
    _description = 'gestion joueur'
    nomJoueur = fields.Char('Nom Joueur', size=8 ,required=True)
    nomPays = fields.Many2one('gestion.pays','Nom Pays')
    poste = fields.Char('Poste',size=8, required=True)
    dateNaiss = fields.Date('Date de naissance', required =True)
class StatJoueur(models.Model):
    _name = 'gestion.statmatch'
    _description = 'gestion statmatch'
    nomJoueur = fields.Many2one('gestion.joueur','Nom Joueur')
    nomPays = fields.Many2one('gestion.pays','Nom Pays')
    annee =  fields.Many2one('gestion.edition','Annee')
    nombreButs = fields.Char('Nomber but',size=8,required=True)
