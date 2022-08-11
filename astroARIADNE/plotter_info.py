from .plotter import SEDPlotter
from extinction import apply


def get_spectrum_model(artist: SEDPlotter):
    """
    Get the spectrum model from the artist.
    """
    Rv = 3.1
    if not artist.norm:
        rad = artist.theta[4]
        dist = artist.theta[3] * u.pc.to(u.solRad)
        norm = (rad / dist) ** 2
        Av = artist.theta[5]
    else:
        norm = artist.theta[3]
        Av = artist.theta[4]
    return artist.spectrum_model
    if artist.grid == 'btcond':
        wave, flux = artist.fetch_btcond()
        lower_lim = 0.125 < wave
        upper_lim = wave < 4.629296073126975
        if artist.irx:
            upper_lim = wave < wave[-1]
        wave = wave[lower_lim * upper_lim]
        flux = flux[lower_lim * upper_lim]
        ext = artist.av_law(wave * 1e4, Av, Rv)
        flx = apply(ext, flux)
        flx *= norm
        return wave, flx
