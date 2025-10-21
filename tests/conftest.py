import pytest
import pandas as pd


@pytest.fixture
def df():
    """
    Fixture to create dummy data for testing.

    :return: A simple DataFrame with sample data.
    :rtype: pd.DataFrame
    """
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, 5, 6],
        'c': [7, 8, 9]
    })
    return df


@pytest.fixture()
def openhub_df():
    """
    Fixture to create dummy data for testing.

    :return: Part of the Openhub Demo Dataframe
    :rtype: pd.DataFrame
    """
    raw_data = [
        {
            "ListeKomponenten": ["K000055"],  # id or material name
            "Massenanteile": None,  # unit g/g
            "Flächenanteilmodifiziert": 0,  # unit %
            "Geometrie": "Quader",  # unit: list of types
            "Kopfraumatmosphäre": None,  # unit list of (pa)
            "Masse": None,  # unit g
            "Verpackungstyp": "Folie",  # type
            "CAD": None,  # link to CAD file
            "RauheitRa": 0.729,  # unit µm
            "RauheitRz": 3.33,  # unit µm
            "Trübung": 450.7,  # unit HLog
            "Glanz": 46.9,  # unit GE
            "Dicke": 777,  # unit µm
            "Emodul": 923.5297844703941,  # unit MPa
            "MaximaleZugspannung": 39.27389962516748,  # unit MPa
            "MaximaleLängenänderung": 24.74862718628088,  # unit %
            # Qulaity Labels
            "Ausformung": 4,
            "Kaltverfo": 2.5,
            # Training Label
            "Temp": 460,
            "Zeit": 56,
            "Druck": 1,
        },
        {
            "ListeKomponenten": ["K000055", "K000057"],
            "Massenanteile": [0.5, 0.5],
            "Flächenanteilmodifiziert": 0,
            "Geometrie": "Quader",
            "Kopfraumatmosphäre": None,
            "Masse": None,
            "Verpackungstyp": "Folie",
            "CAD": None,
            "RauheitRa": 0.08666666666666667,
            "RauheitRz": 0.924,
            "Trübung": 216.1,
            "Glanz": 36.7,
            "Dicke": 738.6666666666666,
            "Emodul": 807.9225728004443,
            "MaximaleZugspannung": 33.22942107172407,
            "MaximaleLängenänderung": 14.57795412214027,
            "Ausformung": 5,
            "Kaltverfo": 3,
            "Temp": 460,
            "Zeit": 40,
            "Druck": 6,
        },
        {
            "ListeKomponenten": ["K000055", "K000057"],
            "Massenanteile": [0.5, 0.5],
            "Flächenanteilmodifiziert": 0,
            "Geometrie": "Quader",
            "Kopfraumatmosphäre": None,
            "Masse": None,
            "Verpackungstyp": "Folie",
            "CAD": None,
            "RauheitRa": 0.08666666666666667,
            "RauheitRz": 0.924,
            "Trübung": 216.1,
            "Glanz": 36.7,
            "Dicke": 738.6666666666666,
            "Emodul": 807.9225728004443,
            "MaximaleZugspannung": 33.22942107172407,
            "MaximaleLängenänderung": 14.57795412214027,
            "Ausformung": 1,
            "Kaltverfo": 3,
            "Temp": 500,
            "Zeit": 8,
            "Druck": 1,
        },
        {
            "ListeKomponenten": ["K000055", "K000057"],
            "Massenanteile": [0.5, 0.5],
            "Flächenanteilmodifiziert": 0,
            "Geometrie": "Quader",
            "Kopfraumatmosphäre": None,
            "Masse": None,
            "Verpackungstyp": "Folie",
            "CAD": None,
            "RauheitRa": 0.08666666666666667,
            "RauheitRz": 0.924,
            "Trübung": 216.1,
            "Glanz": 36.7,
            "Dicke": 738.6666666666666,
            "Emodul": 807.9225728004443,
            "MaximaleZugspannung": 33.22942107172407,
            "MaximaleLängenänderung": 14.57795412214027,
            "Ausformung": 3,
            "Kaltverfo": 1,
            "Temp": 500,
            "Zeit": 12,
            "Druck": 6,
        },
        {
            "ListeKomponenten": ["K000055", "K000057"],
            "Massenanteile": [0.5, 0.5],
            "Flächenanteilmodifiziert": 0,
            "Geometrie": "Quader",
            "Kopfraumatmosphäre": None,
            "Masse": None,
            "Verpackungstyp": "Folie",
            "CAD": None,
            "RauheitRa": 0.08666666666666667,
            "RauheitRz": 0.924,
            "Trübung": 216.1,
            "Glanz": 36.7,
            "Dicke": 738.6666666666666,
            "Emodul": 807.9225728004443,
            "MaximaleZugspannung": 33.22942107172407,
            "MaximaleLängenänderung": 14.57795412214027,
            "Ausformung": 5,
            "Kaltverfo": 3,
            "Temp": 500,
            "Zeit": 32,
            "Druck": 2.67,
        },
        {
            "ListeKomponenten": ["K000055", "K000057"],
            "Massenanteile": [0.5, 0.5],
            "Flächenanteilmodifiziert": 0,
            "Geometrie": "Quader",
            "Kopfraumatmosphäre": None,
            "Masse": None,
            "Verpackungstyp": "Folie",
            "CAD": None,
            "RauheitRa": 0.08666666666666667,
            "RauheitRz": 0.924,
            "Trübung": 216.1,
            "Glanz": 36.7,
            "Dicke": 738.6666666666666,
            "Emodul": 807.9225728004443,
            "MaximaleZugspannung": 33.22942107172407,
            "MaximaleLängenänderung": 14.57795412214027,
            "Ausformung": 6,
            "Kaltverfo": 3,
            "Temp": 500,
            "Zeit": 36,
            "Druck": 6,
        },
        {
            "ListeKomponenten": ["K000055", "K000057"],
            "Massenanteile": [0.5, 0.5],
            "Flächenanteilmodifiziert": 0,
            "Geometrie": "Quader",
            "Kopfraumatmosphäre": None,
            "Masse": None,
            "Verpackungstyp": "Folie",
            "CAD": None,
            "RauheitRa": 0.08666666666666667,
            "RauheitRz": 0.924,
            "Trübung": 216.1,
            "Glanz": 36.7,
            "Dicke": 738.6666666666666,
            "Emodul": 807.9225728004443,
            "MaximaleZugspannung": 33.22942107172407,
            "MaximaleLängenänderung": 14.57795412214027,
            "Ausformung": 6,
            "Kaltverfo": 3,
            "Temp": 500,
            "Zeit": 40,
            "Druck": 1,
        }]
    df = pd.DataFrame(raw_data)
    return df
