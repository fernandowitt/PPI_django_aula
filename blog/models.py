from django.conf import settings
from django.db import models
from django.utils import timezone


class Character(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	HUMAN='Humano'
	DWARF='Anão'
	ELF='Elfo'
	DRAGONBORN='Draconato'
	ORC='Orc'
	DARKELF='Drow'
	HALFORC='Meio-Orc'
	FAE='Fae'
	RACES_CHOICES = (
		(HUMAN, 'Humano'),
		(DWARF, 'Anão'),
		(ELF, 'Elfo'),
		(DRAGONBORN, 'Draconato'),
		(ORC, 'Orc'),
		(DARKELF, 'Drow'),
		(HALFORC, 'Meio-Orc'),
		(FAE, 'Fae'),
	)
	race = models.CharField(
		max_length=9,
		choices=RACES_CHOICES,
		default=HUMAN,
	)
	MAGE='Mago'
	KNIGHT='Cavaleiro'
	DRUID='Druida'
	CLERIC='Clérigo'
	SORCERER='Feiticeiro'
	RANGER='Atirador'
	ROGUE='Ladino'
	MONK='Monge'
	CHARCLASS_CHOICES = (
		(MAGE, 'Mago'),
		(KNIGHT, 'Cavaleiro'),
		(DRUID, 'Druida'),
		(CLERIC, 'Clérigo'),
		(SORCERER, 'Feiticeiro'),
		(RANGER, 'Atirador'),
		(ROGUE, 'Ladino'),
		(MONK, 'Monge'),
	)
	charclass = models.CharField(
		max_length=10,
		choices=CHARCLASS_CHOICES,
		default=KNIGHT,
	)
	LAWFULGOOD='Lawful Good'
	NEUTRALGOOD='Neutral Good'
	CHAOTICGOOD='Chaotic Good'
	LAWFULNEUTRAL='Lawful Neutral'
	TRUENEUTRAL='True Neutral'
	CHAOTICNEUTRAL='Chaotic Neutral'
	LAWFULEVIL='Lawful Evil'
	NEUTRALEVIL='Neutral Evil'
	CHAOTICEVIL='Chaotic Evil'
	ALIGNMENTS_CHOICES=(
		(LAWFULGOOD, 'Lawful Good'),
		(NEUTRALGOOD, 'Neutral Good'),
		(CHAOTICGOOD, 'Chaotic Good'),
		(LAWFULNEUTRAL, 'Lawful Neutral'),
		(TRUENEUTRAL, 'True Neutral'),
		(CHAOTICNEUTRAL, 'Chaotic Neutral'),
		(LAWFULEVIL, 'Lawful Evil'),
		(NEUTRALEVIL, 'Neutral Evil'),
		(CHAOTICEVIL, 'Chaotic Evil'),
	)
	alignment = models.CharField(
		max_length=15,
		choices=ALIGNMENTS_CHOICES,
		default=TRUENEUTRAL,
	)

	def saveChar(self):
		self.save();

	def __str__(self):
		return '{} - {}'.format(self.name, self.author)

class Card(models.Model):
	character = models.ForeignKey(Character, on_delete=models.CASCADE)
	strenght = models.IntegerField()
	agility = models.IntegerField()
	intelligence = models.IntegerField()
	dexterity = models.IntegerField()
	wisdom = models.IntegerField()
	charisma = models.IntegerField()
	constitution = models.IntegerField()
	perks = models.TextField()
	spellbook = models.TextField()
	inventary = models.TextField()
	level = models.IntegerField(default=1)
	experience = models.IntegerField(default=0)

	def addXP(self, amount):
		experience += amount
		while experience >= 100:
			experience -= 100
			level += 1

	def saveCard(self):
		self.save()

	def __str__(self):
		return '{} Card'.format(self.character)

class Adventure(models.Model):
	master = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)

class Post(models.Model):
	Adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '{} - {}'.format(self.title, self.text)