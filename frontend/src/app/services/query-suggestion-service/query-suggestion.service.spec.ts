import { TestBed } from '@angular/core/testing';

import {QuerySuggestionConnectionService } from './query-suggestion.service';

describe('QuerySuggestionService', () => {
  let service: QuerySuggestionConnectionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(QuerySuggestionConnectionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
