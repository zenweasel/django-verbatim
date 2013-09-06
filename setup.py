from distutils.core import setup

setup(
    name='django_verbatim',
    version='0.1',
    packages=['verbatim', 'verbatim.templatetags', 'django_verbatim'],
    url='',
    license='MIT',
    author='Brent Hoover',
    author_email='brent@hoover.net',
    description='Add the verbatim template tag so you can escape template tags in your project template',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
