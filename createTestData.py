commands = (
'''CREATE TABLE meting (
  id int PRIMARY KEY,
  xPosition float not null,
  yPosition float not null,
  zPosition float not null,
  xAcceleration float not null,
  yAcceleration float not null,
  zAcceleration float not null,
  created date not null
);
''',
'''
CREATE TABLE patient (
  id int PRIMARY KEY,
  fullName varchar(255) not null,
  leeftijd int not null,
  initialDoses varchar(255),
  bodyMass float
  -- DOKTER ID FK
);
''',
'''
CREATE TABLE dokter (
  id int PRIMARY KEY,
  fullName varchar(255) not null,
  ziekenhuis int not null
  -- PATIENT ID FK
);
''',
'''
CREATE TABLE dosering (
  id int PRIMARY KEY
  -- PATIENT ID FK
);
'''
)
