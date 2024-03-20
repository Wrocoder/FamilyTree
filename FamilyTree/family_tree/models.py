from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=100)


class Person(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='members')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True, null=True)
    education = models.TextField(blank=True)
    occupation = models.TextField(blank=True)
    hobbies = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    notes = models.TextField(blank=True)

    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class FamilyRelationship(models.Model):
    # family relationships
    PARENT = 'parent'
    CHILD = 'child'
    SPOUSE = 'spouse'
    SIBLING = 'sibling'
    GRANDPARENT = 'grandparent'
    GRANDCHILD = 'grandchild'
    AUNT_UNCLE = 'aunt_uncle'
    NIECE_NEPHEW = 'niece_nephew'
    COUSIN = 'cousin'
    RELATIONSHIP_TYPES = [
        (PARENT, 'Parent'),
        (CHILD, 'Child'),
        (SPOUSE, 'Spouse'),
        (SIBLING, 'Sibling'),
        (GRANDPARENT, 'Grandparent'),
        (GRANDCHILD, 'Grandchild'),
        (AUNT_UNCLE, 'Aunt/Uncle'),
        (NIECE_NEPHEW, 'Niece/Nephew'),
        (COUSIN, 'Cousin'),
    ]

    # define relationship
    from_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='from_people')
    to_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='to_people')
    relationship_type = models.CharField(max_length=12, choices=RELATIONSHIP_TYPES)

    class Meta:
        # avoid duplication relationships
        unique_together = ('from_person', 'to_person', 'relationship_type')

    def __str__(self):
        return f"{self.get_relationship_type_display()} from {self.from_person.full_name()} to {self.to_person.full_name()}"

    # @property
    # def is_direct_line(self):
    #     """ It is direct relationship or not """
    #     return self.relationship_type in {self.PARENT, self.CHILD}
    #
    # @property
    # def is_marriage(self):
    #     """ Marriage or not """
    #     return self.relationship_type == self.SPOUSE
