# -*- coding: utf-8 -*-

from importlib import import_module

from lib.common import log

import settings


reverse = False


class ImportedEvents(object):
    '''
    helper class which holds imported events as its attributes
    '''
    pass


def handle_events():
    '''
    loads active events from settings, activates them and result is used for image merging

    @return [(img1, img2, alpha), (img1, img2, alpha)]
    '''

    # first get active events
    events = settings.events[:]
    curr_directory = settings.images_dir[:]

    # import those
    for event in events:

        setattr(ImportedEvents, event, import_module('events.%s' % event))

    # get their provide, only once can be 'folder'
    folder_count = 0
    have_first = False

    for loaded_event in events:

        # this calls loaded_ev.loaded_ev.provides
        event = getattr(ImportedEvents, loaded_event, False)

        if event:

            if event.provides == 'folder':

                # set it so 'folder' providing event goes fist
                have_first = True
                goes_first = loaded_event
                folder_count += 1

    if folder_count > 1:

        log.error('Error while event loading, more than one event provides folder')

        raise Exception('Active events can have only one that provides "folder", check settings.')

    try:

        # service goes_first, first is always 'folder'
        if have_first and goes_first:

            curr_directory = get_event_result(goes_first)

            # remove so it is not loaded again
            events.remove(goes_first)

        to_return = []
        # call other events
        for c_event in events:

            to_return.append(get_event_result(c_event, curr_directory, reverse))

        return to_return

    except AttributeError, e:

        log.error('event error: %r' % (e))

        raise Exception('There seems to be some event handlers accessing directory that is not available, please check settings.')


def get_event_result(event, curr_directory, reverse):
    '''
    calls specified event and returns its result

    @param event: string
    @return event result
    '''

    kwargs = {'dir': curr_directory,
              'reverse': reverse,
              }

    # call ImportedEvents."event".event(**kwargs) - "event" = settings.events[][index]

    return getattr(ImportedEvents, event).event(**kwargs)
