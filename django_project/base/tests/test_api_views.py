from django.test import TestCase
from rest_framework.test import APIRequestFactory
from fish.tests.model_factories import (
    FishCollectionRecordF,
)
from base.tests.model_factories import (
    LocationSiteF,
    TaxonF,
)
from base.api_views.location_site import (
    LocationSiteList,
    LocationSiteDetail,
)
from base.api_views.taxon import TaxonDetail


class TestApiView(TestCase):
    """Test Location site API """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.location_site = LocationSiteF.create(
            pk=1
        )
        self.fish_collection_1 = FishCollectionRecordF.create(
            pk=1,
            original_species_name=u'Test fish species name 1',
            site=self.location_site
        )
        self.fish_collection_2 = FishCollectionRecordF.create(
            pk=2,
            original_species_name=u'Test fish species name 2',
            site=self.location_site
        )

    def test_get_all_location(self):
        view = LocationSiteList.as_view()
        request = self.factory.get('/api/location-site/')
        response = view(request)
        self.assertTrue(len(response.data) > 0)

    def test_get_location_by_id(self):
        view = LocationSiteDetail.as_view()
        pk = '1'
        request = self.factory.get('/api/location-site/' + pk)
        response = view(request, pk)
        self.assertTrue(
            len(response.data['fish_collection_records']) > 1
        )

    def test_get_taxon_by_id(self):
        pk = 1
        taxon = TaxonF.create(
            pk=1,
            common_name=u'Golden fish',
        )
        view = TaxonDetail.as_view()
        request = self.factory.get('/api/taxon/' + str(pk))
        response = view(request, str(pk))
        self.assertEqual(
            taxon.common_name,
            response.data['common_name']
        )
