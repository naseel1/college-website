
{
    'name': "Sample Theme",
    'summary': """
        sample page is here""",
    'description': """
        Long description of module's purpose
    """,
    'author': " My Company",
    'license': 'LGPL-3',
    'website': "http://www.yourcompany.com",
    'category': "Theme",
    'version': "0.1",
    'depends': [
        'website',
        'base_setup',
        'mail',
        'resource',
        'web',
    ],
    'data': [
        'views/home/home.xml',
        'views/home/downloads.xml',
        'views/home/contactus.xml',

        'views/institution/institution.xml',
        'views/institution/about.xml',
        'views/institution/vision.xml',
        'data/website_data.xml',
        'views/institution/history.xml',
        'views/institution/rules.xml',
        'views/institution/emblem.xml',
        'views/institution/principal.xml',
        'views/institution/code.xml',
        'views/institution/fprincipals.xml',
        'views/institution/management.xml',
        'views/institution/pta.xml',
        'views/institution/adstaff.xml',
        'views/institution/scouncil.xml',
        'views/institution/rti.xml',
        'views/institution/organization.xml',
        'views/institution/sister-institution.xml',

        'views/department/department.xml',
        'views/department/english.xml',
        'views/department/commerce.xml',
        'views/department/economics.xml',
        'views/department/microbiology.xml',
        'views/department/biochemistry.xml',
        'views/department/computer-science.xml',
        'views/department/biotechnology.xml',
        'views/department/business-administration.xml',
        'views/department/mathematics.xml',
        'views/department/west-asian-studies.xml',
        'views/department/logistic.xml',
        'views/department/accounting.xml',

        'views/academics/academics.xml',
        'views/academics/programmes.xml',
        'views/academics/ug-admission.xml',
        'views/academics/pg-admission.xml',
        'views/academics/certificate.xml',
        'views/academics/learning-management.xml',
        'views/academics/calendar.xml',
        'views/academics/human-values.xml',

        'views/students zone/students-zone.xml',
        'views/students zone/nss.xml',
        'views/students zone/ncc.xml',
        'views/students zone/clubs.xml',
        'views/students zone/student-support.xml',
        'views/students zone/capability.xml',
        'views/students zone/student-discipline.xml',
        'views/students zone/student-union.xml',
        'views/students zone/scholarship.xml',
        'views/students zone/college-magazines.xml',
        'views/students zone/attendance-portal.xml',

        'views/research/research.xml',
        'views/research/research-committee.xml',
        'views/research/research-depts.xml',
        'views/research/code-of-ethics.xml',
        'views/research/research-scholars.xml',
        'views/research/research-project.xml',
        'views/research/publication.xml',
        'views/research/journal.xml',

        'views/facilities/facilities.xml',
        'views/facilities/laboratory/laboratories.xml',
        'views/facilities/laboratory/ca-lab.xml',
        'views/facilities/laboratory/msc-biology.xml',
        'views/facilities/laboratory/bsc-biology.xml',
        'views/facilities/laboratory/bio-chem.xml',
        'views/facilities/laboratory/bio-tech.xml',
        'views/facilities/laboratory/language.xml',

        'views/facilities/academic support/academic-support.xml',
        'views/facilities/academic support/administrative-office.xml',
        'views/facilities/academic support/well-equipped.xml',
        'views/facilities/academic support/a-departments.xml',
        'views/facilities/academic support/auditorium.xml',
        'views/facilities/academic support/seminar-hall.xml',
        'views/facilities/academic support/exam-hall.xml',
        'views/facilities/academic support/open-air-class-room.xml',
        'views/facilities/academic support/open-air-theatre.xml',
        'views/facilities/academic support/class-room-announcement.xml',
        'views/facilities/academic support/server-room.xml',

        'views/facilities/Hostels and Retiring Rooms/mens-hostel.xml',
        'views/facilities/Hostels and Retiring Rooms/ladies-hostel.xml',
        'views/facilities/Hostels and Retiring Rooms/guest-room.xml',
        'views/facilities/Hostels and Retiring Rooms/guest-retiring.xml',
        'views/facilities/Hostels and Retiring Rooms/girls-retiring.xml',
        'views/facilities/Hostels and Retiring Rooms/ladies-retiring.xml',

        'views/facilities/Sports Games/vollyball.xml',
        'views/facilities/Sports Games/badminton.xml',
        'views/facilities/Sports Games/gym.xml',
        'views/facilities/Sports Games/handball.xml',
        'views/facilities/Sports Games/shuttle.xml',
        'views/facilities/Sports Games/sports-games.xml',
        'views/facilities/Sports Games/basketball.xml',
        'views/facilities/Sports Games/tennis.xml',

        'views/facilities/eco friendly/solar.xml',
        'views/facilities/eco friendly/bamboo.xml',
        'views/facilities/eco friendly/biogas.xml',
        'views/facilities/eco friendly/water-purification.xml',
        'views/facilities/eco friendly/herbal.xml',
        'views/facilities/eco friendly/horticulture.xml',
        'views/facilities/eco friendly/incinerator.xml',
        'views/facilities/eco friendly/mahagony-park.xml',
        'views/facilities/eco friendly/rain-water.xml',

        'views/facilities/General Facilities/biometric-system.xml',
        'views/facilities/General Facilities/cafeteria.xml',
        'views/facilities/General Facilities/campus-wi-fi.xml',
        'views/facilities/General Facilities/canteen.xml',
        'views/facilities/General Facilities/car-parking.xml',
        'views/facilities/General Facilities/cctv-surveillance.xml',
        'views/facilities/General Facilities/co-operative-store.xml',
        'views/facilities/General Facilities/conveyance.xml',
        'views/facilities/General Facilities/counseling-centre.xml',
        'views/facilities/General Facilities/open-stage.xml',

        'views/MHRD/mhrd.xml',
        'views/MHRD/ugc.xml',
        'views/MHRD/ariia.xml',
        'views/MHRD/aishe.xml',
        'views/MHRD/nirf.xml',
        'views/MHRD/pfms.xml',
        'views/MHRD/rusa.xml',

        'views/Alumni/alumni.xml',
        'views/Alumni/osaemea.xml',
        'views/Alumni/osaemea-chapter1.xml',
        'views/Alumni/osaemea-chapter2.xml',
        'views/Alumni/osaemea-chapter3.xml',
        'views/Alumni/osaemea-website.xml',


        'views/Library/library.xml',
        'views/Library/library-members.xml',
        'views/Library/library-website.xml',

        'views/IQAC/iqac.xml',
        'views/IQAC/composition.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',
        # 'views/IQAC/iqac.xml',















    ],
    'assets': {
        'web.assets_frontend': [
            '/sample_theme/static/css/vision.css',

        ],

    }
}
